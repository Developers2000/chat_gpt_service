from fastapi.encoders import jsonable_encoder


async def add_key(request, body):
    body_encoder = jsonable_encoder(body)
    openai_key = await request.app.chatgpt["keys"].insert_one(body_encoder)
    openai_key = await request.app.chatgpt["keys"].find_one(
        {"_id": openai_key.inserted_id}
    )
    return openai_key


async def get_key_by_user_id(request, user_id):
    openai_key = await request.app.chatgpt["keys"].find_one({"user_id": user_id})
    return openai_key
