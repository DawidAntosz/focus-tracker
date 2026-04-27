# --- STAGE: Build ---
FROM python:3.14.4-alpine3.22 AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_PROJECT_ENVIRONMENT=/install

WORKDIR /app

RUN apk add --no-cache \
    build-base \
    postgresql-dev \
    musl-dev \
    gcc \
    python3-dev

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

COPY . .
RUN uv run ruff check .


# --- STAGE: Final ---
FROM python:3.14.4-alpine3.22

WORKDIR /app

RUN apk add --no-cache libpq

COPY --from=builder /install /install
COPY . .

ENV PATH="/install/bin:$PATH"
ENV PYTHONUNBUFFERED=1

EXPOSE 8080

CMD ["python", "app.py"]