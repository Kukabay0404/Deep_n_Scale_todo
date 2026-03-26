import uuid

from fastapi_users import schemas
from pydantic import Field

class UserRead(schemas.BaseUser[uuid.UUID]):
    
    username : str = Field(min_length=1, max_length=120)


class UserCreate(schemas.BaseUserCreate):
    username : str = Field(min_length=1, max_length=120)


class UserUpdate(schemas.BaseUserUpdate):
    username : str | None = Field(min_length=1, max_length=120, default=None)

