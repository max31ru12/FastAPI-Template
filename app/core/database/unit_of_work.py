from app.core.database.setup_db import session_factory


class SQLAlchemyUnitOfWork:
    def __init__(self):
        self._session = session_factory()

    async def __aenter__(self):
        return self  # Возвращает сам объект, чтобы можно было использовать внутри контекстного менеджера async with

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:  # тип ошибки, если она произошла
            await self.rollback()
        else:
            await self.commit()

    async def rollback(self):
        await self._session.rollback()

    async def commit(self):
        await self._session.commit()
