from abc import ABC, abstractmethod

from psycopg.errors import UniqueViolation
from sqlalchemy import select, update, insert
from sqlalchemy.exc import IntegrityError

from app.core.exceptions import DuplicateError, DatabaseException
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

    @abstractmethod
    async def update(self, db_model_instance: type[Base], where_data: dict, values: dict):
        pass

    @abstractmethod
    async def insert(self, db_model_instance: type[Base], **values):
        pass

    @abstractmethod
    async def commit(self):
        pass


class SqlAlchemyFacade(DatabaseFacade):
    def __init__(self):
        self.db = AsyncSessionLocal()

    async def save(self, db_model_instance: Base):
        try:
            self.db.add(db_model_instance)
            await self.db.commit()
            await self.db.refresh(db_model_instance)
        except IntegrityError as e:
            await self.db.rollback()
            if isinstance(e.orig, UniqueViolation):
                raise DuplicateError('This element already exists')
            raise DatabaseException('DB error')

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

    async def update(self, db_model_instance: type[Base], id: int, values: dict):
        stmt = (
            update(db_model_instance)
            .where(getattr(db_model_instance, 'id') == id)
            .values(**values)
            .returning(db_model_instance)
        )
        result = await self.db.execute(stmt)
        updated_data = result.scalar_one()

        return updated_data

    async def insert(self, db_model_instance: type[Base], **values):
        stmt = insert(db_model_instance).values(**values)

        await self.db.execute(stmt)

    async def commit(self):
        await self.db.commit()