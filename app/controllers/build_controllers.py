from fastapi.encoders import jsonable_encoder
from app.controllers.key_controllers import get_openai_key_by_user_id
import openai


async def build_learning_path(request, body):
    openai_key = await get_openai_key_by_user_id(request, body.user_id)
    print(openai_key["key"], type(openai_key))
    openai.api_key = openai_key["key"]

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", prompt=[{"role":"user", "content": body.message}], max_tokens=80)
    print(chat_completion)

    response = {
        "message": "message",
    }

    return response
