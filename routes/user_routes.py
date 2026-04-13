from fastapi import APIRouter, HTTPException

from services.user_service import (
    create_user,
    get_users,
    get_user,
    update_user,
    delete_user
)

router = APIRouter(prefix="/users", tags=["Users"])


# CREATE
@router.post("/")
async def create(data: dict):
    user = await create_user(data)
    return user


# READ ALL
@router.get("/")
async def read_all():
    return await get_users()


# READ ONE
@router.get("/{user_id}")
async def read_one(user_id: str):
    user = await get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# UPDATE
@router.put("/{user_id}")
async def update(user_id: str, data: dict):
    user = await update_user(user_id, data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# DELETE
@router.delete("/{user_id}")
async def delete(user_id: str):
    success = await delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}