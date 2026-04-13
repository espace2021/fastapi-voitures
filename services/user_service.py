from models.user import User
from typing import List, Optional


# CREATE
async def create_user(data: dict) -> User:
    user = User(**data)
    await user.insert()
    return user


# READ ALL
async def get_users() -> List[User]:
    return await User.find_all().to_list()


# READ ONE
async def get_user(user_id: str) -> Optional[User]:
    return await User.get(user_id)


# UPDATE
async def update_user(user_id: str, data: dict) -> Optional[User]:
    user = await User.get(user_id)
    if not user:
        return None

    # mise à jour des champs
    for key, value in data.items():
        setattr(user, key, value)

    await user.save()
    return user


# DELETE
async def delete_user(user_id: str) -> bool:
    user = await User.get(user_id)
    if not user:
        return False

    await user.delete()
    return True