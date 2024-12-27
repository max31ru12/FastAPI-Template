# README

## Запустить приложение

Сбилдить контейнеры

```shell
docker compose -f ./local.yml up --build -d
```

Провести миграции:

```shell
docker compose -f ./local.yml run --rm backend alembic upgrade head
```


### Создание моделей

Для проведения миграций необходимо выполнить 3 действия:

1. Импортировать модель в `__init__py` модуля `models`, чтобы alembic видел эту модель и провел миграцию создания модели

2. Создать миграцию:

    ```shell
    docker compose -f ./local.yml run --rm backend alembic revision --autogenerate -m "name" --rev-id "001"
    ```

3. Провести миграцию

    ```shell
    docker compose -f ./local.yml run --rm backend alembic upgrade head
    ```

где  `backend` - это имя сервиса


## Сервисы

- http://127.0.0.1:8000/docs - документация API
- на порту `5432` доступна БД postgres


## Links

- [Unique Constraint Naming conventions](https://docs.sqlalchemy.org/en/20/core/constraints.html#constraint-naming-conventions)
