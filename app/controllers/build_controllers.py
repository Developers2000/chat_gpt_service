from fastapi.encoders import jsonable_encoder
import tiktoken
from app.controllers.key_controllers import get_openai_key_by_user_id
import openai


def nums_token_from_message(messages, model="gpt-3.5-turbo-0301"):
    encoding = tiktoken.encoding_for_model(model)
    nums_token = 0
    for message in messages:
        nums_token += 4
        for key, value in message.items():
            nums_token += len(encoding.encode(value))
            if key == "name":
                nums_token += -1
    
    nums_token += 2
    return nums_token

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
