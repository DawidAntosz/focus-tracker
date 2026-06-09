from sqlalchemy.orm import sessionmaker
from .base import BaseRepository

class UserSettingsRepository(BaseRepository):
    def __init__(self, session_factory: sessionmaker):
        super().__init__(session_factory)
