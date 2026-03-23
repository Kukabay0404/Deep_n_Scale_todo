from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
import uuid


class CategoryCreate(BaseModel):
    category_name : str
    owner_id : uuid.UUID


class CategoryUpdate(BaseModel):
    category_name : str | None = Field(default=None)
    owner_id : uuid.UUID | None = Field(default=None)


class CategoryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    category_name : str
    created_at : datetime
    owner_id : uuid.UUID
    