import asyncio
from .configs import settings
from .routers import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router, prefix="/api/v1")


@app.on_event("startup")
async def startup():
    app.mongodb_golive_client = AsyncIOMotorClient(settings.DB_URL_GOLIVE)
    app.mongodb_chatgpt_client = AsyncIOMotorClient(settings.DB_URL_CHATGPT)
    app.golive = app.mongodb_golive_client[settings.DB_NAME_GOLIVE]
    app.chatgpt = app.mongodb_chatgpt_client[settings.DB_NAME_CHATGPT]


@app.on_event("shutdown")
async def shutdown():
    tasks = [
        app.mongodb_golive_client.close(),
        app.mongodb_chatgpt_client.close()
    ]

    await asyncio.gather(*tasks)
