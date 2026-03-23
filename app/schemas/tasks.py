from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field, ConfigDict
import uuid


class TaskCreate(BaseModel):
    user_id : uuid.UUID
    category_id : int
    title : str
    description : str | None = Field(default=None)
    status : Literal['todo', 'in_progress', 'done']
    priority : int | None = Field(ge=1, le=5, description="Приоритет задачи от 1 до 5", default=2)
    due_date : datetime | None = Field(default=None)

class TaskUpdate(BaseModel):
    category_id : int | None = Field(default=None)
    title : str | None = Field(default=None)
    description : str | None = Field(default=None)
    status : Literal['todo', 'in_progress', 'done'] | None = Field(default=None)
    priority : int | None = Field(ge=1, le=5, description="Приоритет задачи от 1 до 5", default=2)
    due_date : datetime | None = Field(default=None)


class TaskOut(BaseModel):

    model_config = ConfigDict(from_attributes=True)
    
    user_id : uuid.UUID
    category_id : int
    title : str
    description : str | None
    status : str
    priority : int
    due_date : datetime | None
    completed_at : datetime | None
    created_at : datetime
    updated_at : datetime
