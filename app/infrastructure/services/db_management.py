from abc import ABC, abstractmethod

from sqlalchemy import select

from app.infrastructure.database.base import Base
from app.infrastructure.database.database import AsyncSessionLocal


class DatabaseFacade(ABC):
    @abstractmethod
    async def save(self, db_model_instance: Base):
        pass

    @abstractmethod
    async def list(self, db_model_instance: type[Base]):
        pass

    @abstractmethod
    async def list_active(self, db_model_instance: type[Base]):
        pass

    @abstractmethod
    async def get_by_id(self, db_model_instance: type[Base], id: int):
        pass


class SqlAlchemyFacade(DatabaseFacade):
    def __init__(self):
        self.db = AsyncSessionLocal()

    async def save(self, db_model_instance: Base):
        self.db.add(db_model_instance)
        await self.db.commit()
        await self.db.refresh(db_model_instance)

        return db_model_instance

    async def list(self, db_model_instance: type[Base]):
        query = select(db_model_instance)
        result = await self.db.execute(query)

        return list(result.scalars().all())


    async def list_active(self, db_model_instance: type[Base]):
        query = select(db_model_instance).where(db_model_instance.is_active.is_(True))
        result = await self.db.execute(query)

        return list(result.scalars().all())

    async def get_by_id(self, db_model_instance: type[Base], id: int):
        query = select(db_model_instance).where(db_model_instance.id == id)
        result = await self.db.execute(query)

        return result.scalars().first()
