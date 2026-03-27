import uuid
from typing import Literal

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.users import User


async def get_users(db: AsyncSession) -> list[User]:
    result = await db.execute(select(User).order_by(User.created_at.desc()))
    return result.scalars().all()


async def _get_user_or_404(user_id: uuid.UUID, db: AsyncSession) -> User:
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def _set_user_flag(
    user_id: uuid.UUID,
    field: Literal["is_active", "is_superuser", "is_verified"],
    value: bool,
    db: AsyncSession,
) -> User:
    user = await _get_user_or_404(user_id, db)
    setattr(user, field, value)

    try:
        await db.commit()
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    await db.refresh(user)
    return user


async def set_user_active(user_id: uuid.UUID, is_active: bool, db: AsyncSession) -> User:
    return await _set_user_flag(user_id, "is_active", is_active, db)


async def set_user_superuser(user_id: uuid.UUID, is_superuser: bool, db: AsyncSession) -> User:
    return await _set_user_flag(user_id, "is_superuser", is_superuser, db)


async def set_user_verified(user_id: uuid.UUID, is_verified: bool, db: AsyncSession) -> User:
    return await _set_user_flag(user_id, "is_verified", is_verified, db)
