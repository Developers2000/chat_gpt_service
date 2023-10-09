from fastapi import APIRouter
from .user_routers import router as user_routers
from .build_routers import router as build_routers

router = APIRouter()

router.include_router(user_routers, tags=["users"], prefix="/users")
router.include_router(build_routers, tags=["builds"], prefix="/builds")
