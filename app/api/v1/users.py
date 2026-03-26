from fastapi import APIRouter

from app.auth.router import router as auth_router


router = APIRouter(
    prefix='/users',
    tags=['Users']
)

router.include_router(auth_router)