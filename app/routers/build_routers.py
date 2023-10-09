from fastapi import APIRouter

router = APIRouter()


@router.get("/learning_path")
async def learning_path():
    return {"message": "Learning path"}
