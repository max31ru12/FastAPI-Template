# README

## Запустить приложение


### Поднять backend с помощью docker

Файл local.yml настроен так, чтобы все работало из коробки. Однако такой подход делает локальную разработку неудобной,
если не использовать удаленный интерпретатор.

```shell
docker compose -f ./local.yml up --build -d
```

Провести миграции:

```shell
docker compose -f ./local.yml run --rm backend alembic upgrade head
```


### Поднять backend локально

Полнять БД:

```shell
docker compose -f ./local.yml up postgres -d
```

Далее создаем виртуальное окружение, устанавливаем зависимости:

```shell
pip install -r requirements-dev.txt
```

Убеждаемся, что переменная окружения `DB_HOST` имеет значение `localhost`. В `/app/config.py` она имеет такое значение
по умолчанию, но ее значение берется из файла `.env`


## Создание моделей

Для проведения миграций необходимо выполнить 4 действия:

1. Импортировать модель в `__init__py` модуля `models`, чтобы alembic видел эту модель и провел миграцию создания модели

2. Создать папку `versions` в  папке `alembic`

3. Создать миграцию:

    ```shell
    docker compose -f ./local.yml run --rm backend alembic revision --autogenerate -m "name" --rev-id "001"
    ```

4. Провести миграцию

    ```shell
    docker compose -f ./local.yml run --rm backend alembic upgrade head
    ```

где  `backend` - это имя сервиса


## Сервисы

- http://127.0.0.1:8000/docs - документация API
- на порту `5432` доступна БД postgres


## Links

- [Unique Constraint Naming conventions](https://docs.sqlalchemy.org/en/20/core/constraints.html#constraint-naming-conventions)
