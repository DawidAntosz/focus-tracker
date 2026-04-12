from enum import StrEnum


class PathKey(StrEnum):
    LOGS_FILE = "logs_file"


class EnvKey(StrEnum):
    DB_HOST = "DB_HOST"
    DB_PORT = "DB_PORT"
    DB_USER = "DB_USER"
    DB_PASSWORD = "DB_PASSWORD"
    DB_NAME = "DB_NAME"
    DEBUG = "DEBUG"
