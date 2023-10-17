from fastapi import APIRouter, Request, Body, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


from app.models.build_model import BuildModel, MessageRequest
from app.controllers.build_controllers import build_learning_path
from app.utils.convert import convert_json_of_mongo

router = APIRouter()


@router.post("/learning_path")
async def learning_path(request: Request, body: MessageRequest = Body(...)):
    learning_path = await build_learning_path(request, body)
    if learning_path is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"learning_path": learning_path})

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Can't build learning path")


@router.get("/test/get-users")
async def get_users(request: Request):
    users = await request.app.golive["users"].find({}).to_list(length=20)
    if users is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"users": convert_json_of_mongo(users)})

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Not users found")


@router.post("/conversation")
async def conversation(request: Request, body: MessageRequest = Body(...)):
    conversation = await conversation(request, body)
    if conversation is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"conversation": conversation})

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Can't build conversation")
