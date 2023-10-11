from pydantic import BaseModel, Field
import uuid


class MessageRequest(BaseModel):
    message: str
    user_id: str


class BuildModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
