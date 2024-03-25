from fastapi import APIRouter

from app.api.v1.deposit import router as deposit_router

router = APIRouter()

router.include_router(deposit_router, prefix="/deposit", tags=["deposit"])
