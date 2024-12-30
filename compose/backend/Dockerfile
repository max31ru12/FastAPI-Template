FROM python:3.12-slim

RUN apt-get update -qy

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY requirements-dev.txt ./

RUN pip install -r requirements-dev.txt

COPY ./app ./app
COPY ./alembic ./
COPY alembic.ini ./

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]

EXPOSE 8000
