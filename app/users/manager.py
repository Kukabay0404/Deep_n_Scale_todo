import uuid

from fastapi_users import BaseUserManager, UUIDIDMixin, InvalidPasswordException
from fastapi import Depends, Request

from app.models.users import User
from app.core.config import get_settings
from app.db.session import get_user_db
from app.users.schemas import UserCreate

settings = get_settings()

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.SECRET_TOKEN
    verification_token_secret = settings.VERIFICATION_TOKEN_SECRET
    
    async def validate_password(self, password : str, user : UserCreate | User) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(reason="Password should be at least 8 characters")
        if user.email in password:
            raise InvalidPasswordException(reason="Password should not contain e-mail")
        
    async def on_after_register(self, user : User, request : Request | None = None):
        print(f'User {user.id} has registered')
    
    async def on_after_forgot_password(self, user : User, token : str, request : Request | None = None):
        print(f'User {user.id} has forgot their password. Reset token {token}')
    
    async def on_after_request_verify(self, user : User, token : str, request : Request | None = None):
        print(f'Verification requested for user {user.id}. Verification token {token}')
    

async def get_user_manager(user_db = Depends(get_user_db)):
    yield UserManager(user_db)