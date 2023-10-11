from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.responses import JSONResponse

from app.controllers.key_controllers import add_key
from app.models.key_model import KeyModel

router = APIRouter()


@router.post("/add")
async def add_key_router(request: Request, body: KeyModel = Body(...)):
    openai_key = await add_key(request, body)
    if openai_key is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"openai_key": openai_key})

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Can't add key")
