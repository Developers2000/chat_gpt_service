from fastapi import APIRouter, Request, Body
from app.models.build_model import BuildModel
import app.controllers.build_controllers as build_controllers

router = APIRouter()


@router.get("/learning_path")
async def learning_path(request: Request, body: BuildModel = Body(...)):
    return build_controllers.build_learning_path(request, body)
