from fastapi_users.authentication import (
    AuthenticationBackend, 
    BearerTransport, 
    JWTStrategy
)
from app.core.config import get_settings


settings = get_settings()

bearer_transport = BearerTransport(tokenUrl="/v1/users/auth/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(settings.JWT_SECRET_KEY, settings.ACCESS_TOKEN_EXPIRE_SECONDS)

auth_backend = AuthenticationBackend(
    name='jwt', 
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)