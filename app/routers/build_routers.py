import datetime
from fastapi import APIRouter, Request, Body, status, HTTPException
from fastapi.responses import JSONResponse
from bson import ObjectId


from app.models.build_model import BuildModel
import app.controllers.build_controllers as build_controllers
from app.utils.convert import convert_json_of_mongo

router = APIRouter()


@router.post("/learning_path")
async def learning_path(request: Request, body: BuildModel = Body(...)):
    return build_controllers.build_learning_path(request, body)


@router.get("/test/get-users")
async def get_users(request: Request):
    users = await request.app.golive["users"].find({}).to_list(length=20)
    if users is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"users": convert_json_of_mongo(users)})

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Not users found")
