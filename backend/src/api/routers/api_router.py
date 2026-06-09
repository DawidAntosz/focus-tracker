from fastapi import APIRouter
from .user import user_router
from .task import task_router


api_router = APIRouter(prefix="/api")
api_router.include_router(user_router, tags=["user"])
api_router.include_router(task_router, tags=["task"])
