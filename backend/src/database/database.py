from typing import Generator
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, Session
from .repositories import UserRepository, TaskRepository

import logging
log = logging.getLogger(__name__)


class Database:
    def __init__(
        self,
        db_session_factory: sessionmaker,
        user_repository: UserRepository,
        task_repository: TaskRepository,
    ):
        self._session_factory = db_session_factory
        self.users = user_repository
        self.tasks = task_repository

    @contextmanager
    def transaction(self) -> Generator[Session, None, None]:
        session: Session = self._session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            log.exception("Transaction failed, rolling back changes.")
            raise
        finally:
            session.close()
