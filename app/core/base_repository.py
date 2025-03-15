from abc import ABC, abstractmethod
from typing import Any, Generic, Sequence, TypeVar

from sqlalchemy import delete, select, update
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository(ABC):
    @abstractmethod
    def get_first_by_kwargs(self, **kwargs):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def remove(self, *args):
        pass


T = TypeVar("T")


class SQLAlchemyRepository(BaseRepository, Generic[T]):
    model: T = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(self) -> Sequence[T]:
        stmt = select(self.model)
        return (await self.session.execute(stmt)).scalars().all()

    async def get_first_by_kwargs(self, **kwargs) -> T:
        stmt = select(self.model).filter_by(**kwargs)
        return (await self.session.execute(stmt)).scalars().first()

    async def create(self, **kwargs) -> T:
        instance = self.model(**kwargs)
        self.session.add(instance)
        return instance

    async def update(self, row_id: int, update_data: dict[str | Any]) -> Result[int]:
        return await self.session.execute(
            update(self.model).where(self.model.id == row_id).values(**update_data).returning(self.model.id)
        )

    async def remove(self, row_id: int) -> Result[int]:
        return await self.session.execute(delete(self.model).where(self.model.id == row_id).returning(self.model.id))
