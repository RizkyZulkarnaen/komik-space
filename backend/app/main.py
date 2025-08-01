from fastapi import FastAPI
from app.api.main import api_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from typing import List

app = FastAPI()

if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get('/')
def home():
    return {
        "message" : "hallo dunia"
    }

app.include_router(api_router, prefix=settings.API_V1_STR)