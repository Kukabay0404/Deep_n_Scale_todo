import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.admin.users import get_users, set_user_superuser, set_user_active, set_user_verified
from app.users.schemas import UserRead, UserUpdate
from app.users.deps import current_superuser
from app.users.deps import fastapi_users

router = APIRouter(
    prefix='/admin',
    tags=['Admin'],
    dependencies=[Depends(current_superuser)],
)

@router.get(path='/users', response_model=list[UserRead])
async def list_users(db : AsyncSession = Depends(get_db)):
    return await get_users(db=db)


@router.patch(path='/users/{user_id}/superuser', response_model=UserRead)
async def set_user_superuser_endpoint(
    user_id: uuid.UUID, 
    is_superuser: bool, 
    db: AsyncSession = Depends(get_db)
):
    return await set_user_superuser(user_id, is_superuser, db=db)


@router.patch(path='/users/{user_id}/active', response_model=UserRead)
async def set_user_active_endpoint(
    user_id: uuid.UUID, 
    is_active: bool, 
    db: AsyncSession = Depends(get_db)
):
    return await set_user_active(user_id, is_active, db=db)


@router.post(path='/users/{user_id}/verified', response_model=UserRead)
async def set_user_verified_endpoint(
    user_id: uuid.UUID, 
    is_verified: bool, 
    db: AsyncSession = Depends(get_db)
):
    return await set_user_verified(user_id, is_verified, db=db)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate)
)