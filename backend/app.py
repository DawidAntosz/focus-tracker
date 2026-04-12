import sys
import signal
import uvicorn
from containers import Container
from src.api import create_app


def handle_exit(signum, frame):
    sys.exit(0)


if __name__ == '__main__':
    # --- Dependency Injection
    container = Container()
    container.wire()

    # --- Exit handle
    signal.signal(signal.SIGTERM, handle_exit)
    signal.signal(signal.SIGINT, handle_exit)

    # --- Run app FastAPI
    app = create_app(container)

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000,
        log_level="info"
    )
