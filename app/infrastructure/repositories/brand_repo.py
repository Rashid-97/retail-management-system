from psycopg.errors import UniqueViolation
from sqlalchemy import select, update, insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import DuplicateError, DatabaseException
from app.domain.entities.entity import Brand
from app.domain.repositories.brand import IBrandRepository
from app.infrastructure.database.models import subcompany_brand_association_history
from app.infrastructure.database.models.brand import BrandDB
from app.infrastructure.services.db_management import DatabaseFacade


class BrandRepository(IBrandRepository):
    def __init__(self, db_facade: DatabaseFacade):
        self.db_facade = db_facade

    async def create_brand(self, brand: Brand) -> BrandDB:
        return await self.db_facade.save(BrandDB(**vars(brand)))

    async def list_brand(self) -> list[BrandDB]:
        return await self.db_facade.list(BrandDB)

    async def get_brand_by_id(self, brand_id: int) -> BrandDB:
        return await self.db_facade.get_by_id(BrandDB, brand_id)
        brand_query = select(BrandDB).where(BrandDB.id == brand_id)
        brand_result = await self.db.execute(brand_query)
        brand = brand_result.scalar_one_or_none()

        if not brand:
            raise DatabaseException('This brand doesn\'t exist')

        return brand


class BrandReassignRepository:
    def __init__(self, db_facade: DatabaseFacade):
        self.db_facade = db_facade

    async def reassign_brand(self, brand_id: int, subcompany_id: int) -> BrandDB:
        updated_brand = await self._update_brand_subcompany(brand_id, subcompany_id)
        await self._add_brand_subcompany_reassign_history(brand_id, subcompany_id)

        await self.db_facade.commit()
        return updated_brand

    async def _update_brand_subcompany(self, brand_id: int, subcompany_id: int) -> BrandDB:
        return await self.db_facade.update(db_model_instance=BrandDB,
                                           id=brand_id,
                                           values={'subcompany_id': subcompany_id})


    async def _add_brand_subcompany_reassign_history(self, brand_id: int, subcompany_id: int) -> None:
        await self.db_facade.insert(db_model_instance=subcompany_brand_association_history,
                                    subcompany_id=subcompany_id,
                                    brand_id=brand_id)
