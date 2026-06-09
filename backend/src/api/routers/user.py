from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from containers import Container
from src.utils import Config, Responses, ResponseStatus
from pydantic import BaseModel

from src.database import Database
from src.services import UserService, TaskService

import logging
log = logging.getLogger(__name__)


user_router = APIRouter(
    prefix="/user", 
    tags=["user"]
)

class LoginRequest(BaseModel):
    username: str
    password: str

@user_router.post("/login")
@inject
async def login_user(
    data: LoginRequest,
    user_service: UserService = Depends(Provide[Container.user_service]),
    task_service: TaskService = Depends(Provide[Container.task_service]),
    db_facade: Database = Depends(Provide[Container.database]),
    config: Config = Depends(Provide[Container.config]),
):

    if not config.get("ALLOW_LOGIN", True):
        return Responses.error("Logowanie tymczasowo wyłączone", ResponseStatus.ERROR)

    user = await user_service.authenticate(data.username, data.password)
    
    if not user:
        return Responses.error("Invalid login data", ResponseStatus.ERROR)

    pending_tasks = await task_service.get_user_tasks(user.id)

    return Responses.success(
        {
            "token": "fake-jwt-token",
            "user_id": user.id,
            "tasks_count": len(pending_tasks)
        },
        message="Zalogowano pomyślnie"
    )
