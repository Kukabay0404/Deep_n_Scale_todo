from fastapi import APIRouter, Depends

from app.auth.backend import auth_backend
from app.models.users import User
from app.users.deps import current_active_user, fastapi_users
from app.users.schemas import UserCreate, UserRead, UserUpdate

router = APIRouter(
    prefix="/auth",
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend)
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate)
)

router.include_router(
    fastapi_users.get_verify_router(UserRead)
)

router.include_router(
    fastapi_users.get_reset_password_router()
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate)
)


@router.get("/authenticated_route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}
