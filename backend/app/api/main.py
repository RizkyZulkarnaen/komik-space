from fastapi import APIRouter
from app.api.routers import manga, users

api_router = APIRouter()

api_router.include_router(manga.router)
api_router.include_router(users.router)
