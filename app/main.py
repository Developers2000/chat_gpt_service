import asyncio
from .configs import settings
from .routers import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient


description = """
ChatGPT API helps you build learning path and more. 🚀
"""


app = FastAPI(
    title="ChatGPT API",
    description=description,
    summary="Building learning path and more",
    version="0.0.1",
    contact={
        "name": "Lưu Công Quang Vũ",
        "url": "https://vuluu2k.vercel.app/#contact",
        "email": "vuluu040320@gmail.com",
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router, prefix="/api/v1")


@app.on_event("startup")
def startup():
    app.mongodb_golive_client = AsyncIOMotorClient(settings.DB_URL_GOLIVE)
    app.mongodb_chatgpt_client = AsyncIOMotorClient(settings.DB_URL_CHATGPT)
    app.golive = app.mongodb_golive_client[settings.DB_NAME_GOLIVE]
    app.chatgpt = app.mongodb_chatgpt_client[settings.DB_NAME_CHATGPT]


@app.on_event("shutdown")
def shutdown():
    app.mongodb_golive_client.close()
    app.mongodb_chatgpt_client.close()
