from pydantic import BaseModel, Field
import uuid


class MessageRequest(BaseModel):
    message: str
    user_id: str

    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "example": {
                "message": "Xây dựng lộ trình học Web FontEnd",
                "user_id": "648aedc878cadfbe95c748d7"
            }
        }
    }


class BuildModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    message: str | None = None
    user_id: str | None = None

class ConversationModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    messages: str | None = None
    title: str | None = None
    user_id: str | None = None