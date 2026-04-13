from fastapi import FastAPI
from contextlib import asynccontextmanager

# Imports
from database.db import init_db

from fastapi.middleware.cors import CORSMiddleware

# router API 
from routes.user_routes import router as user_router
from routes.voiture_routes import router as voiture_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = await init_db()
    yield
    client.close()
    print("Connexion MongoDB fermée proprement")


app = FastAPI(
    title="FastAPI + Beanie + PyMongo (structure propre)",
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {"message": "API FastAPI + Beanie bien structurée ! "}

# =========================================================
# CORS CONFIG
# =========================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# ROUTES
# =========================================================
app.include_router(user_router)
app.include_router(voiture_router)