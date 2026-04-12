from dependency_injector import containers, providers

from src.utils import Config
from src.services import UserService, TaskService 
from src.database import Database
from src.database.base import DatabaseSession
from src.database.repositories import UserRepository, TaskRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.api.routers.motion.router",
            "src.api.routers.service.router",
            "src.api.routers.settings.router",
            "src.api.routers.cnc_programs.router",
            "src.api.routers.reports.router"
        ]
    )

    config = providers.Singleton(Config)


    # --- Database
    # Session
    db_session = providers.Singleton(
        DatabaseSession,
        config=config,
    )

    # Repositories
    user_repository = providers.Singleton(
        UserRepository,
        session_factory=db_session.provided.SessionLocal,
    )

    task_repository = providers.Singleton(
        TaskRepository,
        session_factory=db_session.provided.SessionLocal,
    )

    # Persistence Facade
    database = providers.Singleton(
        Database,
        db_session_factory=db_session.provided.SessionLocal,
        user_repository=user_repository,
        task_repository=task_repository,
    )
    # ---


    # --- Services
    user_service = providers.Factory(
        UserService
    )

    task_service = providers.Factory(
        TaskService
    )
    # ---
