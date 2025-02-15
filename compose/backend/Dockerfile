FROM python:3.12.3-slim


RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get remove -y curl && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:$PATH"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY ./alembic ./
COPY alembic.ini ./

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0"]

EXPOSE 8000
