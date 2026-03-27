from fastapi import APIRouter

from app.api.v1.users import router as users_router
from app.api.v1.admin import router as admin_router
from app.api.v1.category import router as category_router

router = APIRouter(
    prefix='/v1'
)

router.include_router(users_router)
router.include_router(admin_router)
router.include_router(category_router)