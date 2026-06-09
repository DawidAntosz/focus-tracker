from logging import DEBUG
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from dependency_injector.containers import DeclarativeContainer

from src.utils import config_logger
from src.database import DatabaseSession
from src.api.routers import api_router


import logging
log = logging.getLogger(__name__)


class AppWithContainer(FastAPI):
    container: DeclarativeContainer


@asynccontextmanager
async def lifespan(app: AppWithContainer):
    container = app.container
    try:
        db_session: DatabaseSession = container.db_connector()
        db_session.check_connection()
    except Exception as e:
        log.error(f"Database initialization failed: {e}")
        raise

    yield

    log.info("Shutting down application...")


def create_app(container: DeclarativeContainer) -> AppWithContainer:
    app = AppWithContainer(
        title="Focus Tracker API",
        version="1.0.0",
        description="API for tracking work sessions and tasks",
        lifespan=lifespan
    )

    # --- Dependency Injector
    app.container = container

    # --- Logger
    config_logger(container.config(), app, level=DEBUG)


    # --- CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # --- Routers
    app.include_router(api_router)

    return app
