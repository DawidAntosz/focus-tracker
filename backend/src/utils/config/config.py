import os
import yaml
from pathlib import Path
from typing import Any, Optional
from dotenv import load_dotenv

from .enums import PathKey, EnvKey
from .constants import Const

import logging
log = logging.getLogger(__name__)


class Config():
    def __init__(self):
        self.config_path: Path = Const.DEFAULT_CONFIG_FILE
        self._load_env()

        self.debug = self._get_bool_env(EnvKey.DEBUG, default=False)

        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found at {self.config_path}")

        self.config_data: dict[str, Any] = self._load_config_yaml()
        self.paths = self.config_data.get("paths", {})

    def _load_env(self) -> None:
        if Const.ENV_FILE.exists():
            load_dotenv(dotenv_path=Const.ENV_FILE)
        else:
            log.warning(f".env file not found: {Const.ENV_FILE}")

    def _load_config_yaml(self) -> dict[str, Any]:
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        try:
            with open(self.config_path, "r") as file:
                return yaml.safe_load(file) or {}
        except yaml.YAMLError as e:
            raise RuntimeError(f"Invalid YAML config: {e}") from e

    def _get_bool_env(self, key: EnvKey, default: bool = False) -> bool:
        value = os.getenv(key.value)
        if value is None:
            return default
        return value.strip().lower() == "true"

    def get_env(self, key: str, default: Optional[str] = None) -> Optional[str]:
        return os.getenv(key, default)

    def get_path(self, key: PathKey) -> Path:
        value = self.paths.get(key)
        if value is None:
            raise KeyError(f"Missing path key: {key}")
        return Path(value)
