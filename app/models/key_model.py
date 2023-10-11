import uuid
from datetime import datetime
from pydantic import BaseModel, Field


class KeyModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    key: str
    user_id: str | None = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "example": {
                "key": "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",
                "user_id": "648aedc878cadfbe95c748d7"
            }
        }
    }
