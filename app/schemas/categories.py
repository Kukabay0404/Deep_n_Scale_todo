from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class CategoryCreate(BaseModel):
    category_name : str


class CategoryUpdate(BaseModel):
    category_name : str | None = Field(default=None)


class CategoryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id : int
    category_name : str
    created_at : datetime
    
