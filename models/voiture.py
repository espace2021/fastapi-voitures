from beanie import Document

class Voiture(Document):
    marque: str # Ex: "Toyota", "Renault", "Ford"
    modele: str # Ex: "Corolla", "Clio", "Mustang"
    annee: int
    prix: float
    kilometrage: int
    type_carburant: str # Ex: "Essence", "Diesel", "Electrique"
    couleur: str
    nombre_portes: int
    transmission: str # Manuelle, Automatique
    options: list[str] = [] # Liste d'options (ex: ["climatisation", "GPS", "toit ouvrant"])
    image_url: str = "" # URL de l'image de la voiture
    statut: str = "disponible" # disponible, vendu, réservé

    class Settings:
        name = "voitures"          # nom de la collection dans MongoDB