# db.py
from pymongo import AsyncMongoClient
from beanie import init_beanie

from models import all_models


async def init_db():
    """Initialise la connexion MongoDB + Beanie"""
    client = AsyncMongoClient("mongodb://localhost:27017/")   # MongoDB en local
    
    await init_beanie(
    database=client["fastapi_beanie_db"],
    document_models=all_models
    ) 
    
    print("Beanie + MongoDB initialisés avec succès (asynchrone)")
    return client