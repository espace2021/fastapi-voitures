from models.voiture import Voiture

# import des services
from services.voiture_service import (
    create_voiture as service_create_voiture,
    get_voitures as service_get_voitures,
    get_voiture as service_get_voiture,
    update_voiture as service_update_voiture,
    delete_voiture as service_delete_voiture,
)


def register_tools(mcp):

    # =========================================================
    # CREATE
    # =========================================================
    @mcp.tool()
    async def create_voiture(data: dict):
        data.pop("id", None)  # laisser Mongo/Beanie générer l'id
        result = await service_create_voiture(data)
        return result.model_dump() if result else None


    # =========================================================
    # READ ALL
    # =========================================================
    @mcp.tool()
    async def get_voitures():
        result = await service_get_voitures()
        return [v.model_dump() for v in result]


    # =========================================================
    # READ ONE
    # =========================================================
    @mcp.tool()
    async def get_voiture_by_id(voiture_id: str):
        result = await service_get_voiture(voiture_id)
        return result.model_dump() if result else None


    # =========================================================
    # UPDATE
    # =========================================================
    @mcp.tool()
    async def update_voiture_by_id(voiture_id: str, data: dict):
        result = await service_update_voiture(voiture_id, data)
        return result.model_dump() if result else None


    # =========================================================
    # DELETE
    # =========================================================
    @mcp.tool()
    async def delete_voiture_by_id(voiture_id: str):
        result = await service_delete_voiture(voiture_id)
        return {"success": result}
    

    # =========================================================
    # TOOL : VOITURE SELON BUDGET
    # =========================================================
    @mcp.tool()
    async def get_voiture_by_budget(budget: float):
        """
        Retourne la meilleure voiture selon un budget donné
        """

        # 1. récupérer toutes les voitures
        voitures = await Voiture.find_all().to_list()

        # 2. filtrer celles dans le budget
        candidates = [
            v for v in voitures
            if v.prix <= budget
        ]

        if not candidates:
            return {
                "message": "Aucune voiture disponible dans ce budget",
                "budget": budget
            }

        # 3. scoring intelligent
        def score(voiture):
            # plus récent = meilleur
            score_year = voiture.annee * 10

            # plus proche du budget = meilleur
            score_price = (budget - voiture.prix)

            return score_year - score_price

        # 4. trier par score
        best = max(candidates, key=score)

        # 5. retourner résultat structuré
        return {
            "budget": budget,
            "voiture": {
                "id": str(best.id),
                "marque": best.marque,
                "modele": best.modele,
                "annee": best.annee,
                "prix": best.prix,
                "kilometrage": best.kilometrage,
                "type_carburant": best.type_carburant,
            }
        }