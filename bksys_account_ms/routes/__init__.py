from fastapi import APIRouter

from .account_routes import router as account_router
from .monitoring import router as monitoring_router

router = APIRouter()
router.include_router(monitoring_router)
router.include_router(account_router)

__all__ = ["router"]
