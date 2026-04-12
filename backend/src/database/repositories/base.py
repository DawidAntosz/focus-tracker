from typing import Optional, Generator
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, Session

import logging
log = logging.getLogger(__name__)


class BaseRepository:
    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory

    @contextmanager
    def session_scope(self, external_session: Optional[Session] = None) -> Generator[Session, None, None]:
        if external_session is not None:
            yield external_session
            return

        session: Session = self.session_factory()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            log.exception("Database error in %s", self.__class__.__name__)
            raise
        finally:
            session.close()
