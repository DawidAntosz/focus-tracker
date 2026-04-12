# --- STAGE: Build ---
FROM python:3.14.4-alpine3.22 AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk add --no-cache \
    build-base \
    postgresql-dev \
    musl-dev \
    gcc \
    python3-dev

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# --- STAGE: Final ---
FROM python:3.14.4-alpine3.22

WORKDIR /app

RUN apk add --no-cache libpq

COPY --from=builder /install /usr/local
COPY . .

EXPOSE 8080

CMD ["python", "app.py"]