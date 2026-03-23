from datetime import datetime

from pydantic import BaseModel, Field, EmailStr, ConfigDict
import uuid


class UserCreate(BaseModel):
    username : str = Field(min_length=1, max_length=120)
    email : EmailStr = Field(min_length=1, max_length=64)
    password : str = Field(min_length=1, max_length=120)


class UserUpdate(BaseModel):
    username : str | None = Field(min_length=1, max_length=120, default=None)
    email : EmailStr | None = Field(min_length=1, max_length=64, default=None)
    password : str | None = Field(min_length=1, max_length=120, default=None)


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id : uuid.UUID
    username : str
    email : str
    is_active : bool
    created_at : datetime
    updated_at : datetime