from fastapi import APIRouter, Depends
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models.users import User
from app.users.deps import current_active_user
from app.schemas.categories import CategoryCreate, CategoryOut, CategoryUpdate


from app.crud.category import (
    return_all_categories, 
    get_category,
    create_category,
    update_category, 
    delete_category
)

router = APIRouter(
    prefix='/categories',
    tags=['Category'],
    dependencies=[Depends(current_active_user)]
)

@router.get('/', response_model=list[CategoryOut], status_code=200)
async def get_all_categories(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    return await return_all_categories(owner_id=user.id, db=db)


@router.get('/{category_id}', response_model=CategoryOut)
async def get_category_for_user(
    category_id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    return await get_category(category_id=category_id, owner_id=user.id, db=db)

@router.post('/', response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
async def create_category_for_user(
    category: CategoryCreate,
    user: User = Depends(current_active_user),
    db: AsyncSession = Depends(get_db),
):
    return await create_category(category_scheme=category, owner_id=user.id, db=db)

@router.patch('/{category_id}', response_model=CategoryOut)
async def update_category_for_user(
    category_id: int,
    category_scheme: CategoryUpdate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    return await update_category(
        category_id=category_id,
        category_scheme=category_scheme,
        owner_id=user.id,
        db=db,
    )

@router.delete('/{category_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_category_for_user(
    category_id: int,
    user: User = Depends(current_active_user),
    db: AsyncSession = Depends(get_db),
):
    return await delete_category(owner_id=user.id, category_id=category_id, db=db)
