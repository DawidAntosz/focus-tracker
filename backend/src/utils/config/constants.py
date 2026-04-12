from pathlib import Path


class Const:
    CURRENT_DIR: Path = Path(__file__).resolve().parent
    BASE_DIR: Path = CURRENT_DIR.parent.parent.parent

    DEFAULT_CONFIG_FILE: Path = CURRENT_DIR / "config.yaml"
    ENV_FILE: Path = BASE_DIR / ".env"

    PROJECT_ROOT: Path = BASE_DIR
