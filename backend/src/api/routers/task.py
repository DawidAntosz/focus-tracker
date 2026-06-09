from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from containers import Container
from src.utils import Config, Responses, ResponseStatus
from src.services import TaskService

import logging
log = logging.getLogger(__name__)


task_router = APIRouter(
    prefix="/task", 
    tags=["task"]
)


@task_router.get("/{task_id}")
@inject
async def get_task_details(
    task_id: int,
    config: Config = Depends(Provide[Container.config]),
    task_service: TaskService = Depends(Provide[Container.task_service]) 
):
    app_name = config.get("APP_NAME", "Backend App")
    task = await task_service.get_task_by_id(task_id)

    if not task:
        return Responses.error(
            message="", 
            status_code=ResponseStatus.ERROR
        )

    return Responses.success(
        data={"task": task, "source": app_name},
        message="Pobrano dane zadania"
    )
