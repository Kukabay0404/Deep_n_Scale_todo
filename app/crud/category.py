import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.schemas.categories import CategoryCreate, CategoryUpdate
from app.models.categories import Category


async def return_all_categories(owner_id: uuid.UUID, db: AsyncSession) -> list[Category]:
    res = await db.execute(
        select(Category).where(Category.owner_id == owner_id)
    )
    return res.scalars().all()

async def get_category(category_id: int, owner_id: uuid.UUID, db: AsyncSession) -> Category:
    res = await db.execute(
        select(Category).where(
            Category.id == category_id,
            Category.owner_id == owner_id,
        )
    )
    category = res.scalar_one_or_none()

    if not category:
        raise HTTPException(status_code=404, detail='Category not found')

    return category

async def create_category(category_scheme: CategoryCreate, owner_id: uuid.UUID, db: AsyncSession) -> Category:
    res = await db.execute(
        select(Category).where(
            Category.category_name == category_scheme.category_name,
            Category.owner_id == owner_id,
        )
    )
    checking = res.scalar_one_or_none()
    if checking:
        raise HTTPException(status_code=409, detail='Category already exists')

    category = Category(
        category_name=category_scheme.category_name,
        owner_id=owner_id
    )

    db.add(category)
    await db.commit()
    await db.refresh(category)

    return category

async def update_category(
    category_id: int,
    category_scheme: CategoryUpdate,
    owner_id: uuid.UUID,
    db: AsyncSession,
) -> Category:
    category = await get_category(category_id=category_id, owner_id=owner_id, db=db)

    update_data = category_scheme.model_dump(exclude_unset=True)

    if "category_name" in update_data:
        res = await db.execute(
            select(Category).where(
                Category.category_name == update_data["category_name"],
                Category.owner_id == owner_id,
                Category.id != category_id,
            )
        )
        existing_category = res.scalar_one_or_none()
        if existing_category:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Category already exists",
            )

    for key, value in update_data.items():
        setattr(category, key, value)

    await db.commit()
    await db.refresh(category)

    return category

async def delete_category(owner_id: uuid.UUID, category_id: int, db: AsyncSession) -> None:
    category = await get_category(category_id=category_id, owner_id=owner_id, db=db)

    await db.delete(category)
    await db.commit()

    return None
    
