from fastapi import APIRouter
from app import models, schemas, crud

router = APIRouter(prefix="/users")

@router.post("/add")
async def create_new_user():
    return {"data" : "hallo"}