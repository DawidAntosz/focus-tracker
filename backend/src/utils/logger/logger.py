import os
import logging
from pathlib import Path
from logging import StreamHandler, Formatter, LogRecord
from fastapi import FastAPI
from logging.handlers import TimedRotatingFileHandler
from src.utils import Config, PathKey


DEFAULT_FORMAT = "[%(asctime)s][%(levelname)s][%(name)s] %(message)s"
SRC_FORMAT = "[%(asctime)s][%(levelname)s][%(name)s:%(lineno)d] %(message)s"


class CustomFormatter(Formatter):
    def __init__(self):
        super().__init__()
        self.default_formatter = Formatter(DEFAULT_FORMAT)
        self.src_formatter = Formatter(SRC_FORMAT)

    def format(self, record: LogRecord) -> str:
        if record.name.startswith("src."):
            return self.src_formatter.format(record)
        return self.default_formatter.format(record)


def _create_file_handler(log_file: Path, formatter: Formatter) -> TimedRotatingFileHandler:
    handler = TimedRotatingFileHandler(
        filename=log_file,
        when="midnight",
        backupCount=30,
        encoding="utf-8",
    )
    handler.suffix = "%Y-%m-%d.log"
    handler.setFormatter(formatter)
    return handler


def _create_console_handler(formatter: Formatter) -> StreamHandler:
    handler = StreamHandler()
    handler.setFormatter(formatter)
    return handler


def config_logger(config: Config, app: FastAPI, level: int = logging.INFO) -> None:
    log_file: Path = config.get_path(PathKey.LOGS_FILE)
    os.makedirs(log_file.parent, exist_ok=True)

    formatter = CustomFormatter()

    file_handler = _create_file_handler(log_file, formatter)
    console_handler = _create_console_handler(formatter)

    root_logger = logging.getLogger()

    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    root_logger.setLevel(level)

    app.state.logger = root_logger
