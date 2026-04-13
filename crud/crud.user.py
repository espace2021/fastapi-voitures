from fastapi import FastAPI, HTTPException, Query
from models import User
from crud import (
    create_user,
    list_users,
    get_user_by_email,
    update_user,
    delete_user,
)
# ==================== ROUTES USERS ====================

@app.post("/users/", response_model=User)
async def create_new_user(user: User):
    # Vérification email unique (Beanie gère déjà l'index unique)
    existing = await get_user_by_email(user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email déjà utilisé")
    
    return await create_user(user)


@app.get("/users/", response_model=List[User])
async def get_all_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100)
):
    return await list_users(skip=skip, limit=limit)


@app.get("/users/email/{email}", response_model=User)
async def get_user_by_email_route(email: str):
    user = await get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user


@app.put("/users/{user_id}", response_model=User)
async def update_existing_user(user_id: str, update_data: dict):
    user = await update_user(user_id, update_data)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user


@app.delete("/users/{user_id}")
async def delete_existing_user(user_id: str):
    deleted = await delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return {"message": "Utilisateur supprimé avec succès"}