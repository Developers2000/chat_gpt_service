from fastapi.encoders import jsonable_encoder
# import tiktoken
from app.controllers.key_controllers import get_openai_key_by_user_id
# import openai

# openai.api_key = "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"
# openai.api_base = "http://localhost:1337"


import g4f, asyncio

_providers = [
    g4f.Provider.Aichat,
    g4f.Provider.ChatBase,
    g4f.Provider.Bing,
    g4f.Provider.GptGo,
    # g4f.Provider.You,
    # g4f.Provider.Yqcloud,
]
 

async def run_provider(provider: g4f.Provider.BaseProvider, message: str = "Hello"):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": message}],
            provider=provider,
        )

        return {f"{provider.__name__}": response}
    except Exception as e:
        return {f"{provider.__name__}": e}
        
async def run_all(message: str = "Hello"):
    calls = [
        run_provider(provider, message) for provider in _providers
    ]
    return await asyncio.gather(*calls)



async def build_learning_path(request, body):
    responses = await run_all(body.message)


    return {"responses" : responses}
