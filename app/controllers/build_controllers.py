from fastapi.encoders import jsonable_encoder
from app.controllers.key_controllers import get_openai_key_by_user_id
import openai


async def build_learning_path(request, body):
    body_encoder = jsonable_encoder(body)
    openai_key = await get_openai_key_by_user_id(request, body["user_id"])
    openai.api_key = openai_key

    response = {
        "message": "message",
    }

    return response
