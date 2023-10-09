from pydantic import BaseModel, Field
import uuid


class BuildModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    message: str = Field(...)
    user_id: str = Field(...)
