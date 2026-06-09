from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from src.utils.config import Config, EnvKey

import logging
log = logging.getLogger(__name__)


class DatabaseSession:
    def __init__(self, config: Config):
        self.config = config

        db_url = URL.create(
            drivername="postgresql+psycopg2",
            username=self.config.get_env(EnvKey.DB_USER),
            password=self.config.get_env(EnvKey.DB_PASSWORD),
            host=self.config.get_env(EnvKey.DB_HOST),
            port=int(self.config.get_env(EnvKey.DB_PORT, "5432")),
            database=self.config.get_env(EnvKey.DB_NAME),
        )

        engine_args = {
            "pool_pre_ping": True,
            "pool_size": 10,
            "max_overflow": 20,
        }

        self.engine = create_engine(db_url, **engine_args)

        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

    def check_connection(self):
        try:
            with self.engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            log.info("Database connection check successful.")
        except Exception as e:
            log.error(f"Database connection check failed: {e}")
            raise e
