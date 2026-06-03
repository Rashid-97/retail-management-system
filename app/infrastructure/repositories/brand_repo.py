from psycopg.errors import UniqueViolation
from sqlalchemy import select, update, insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import DuplicateError, DatabaseException
from app.domain.entities.entity import Brand
from app.domain.repositories.brand import IBrandRepository
from app.infrastructure.database.models import subcompany_brand_association_history
from app.infrastructure.database.models.brand import BrandDB


class BrandRepository(IBrandRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_brand(self, brand: Brand) -> BrandDB:
        db_brand = BrandDB(**vars(brand))
        try:
            self.db.add(db_brand)
            await self.db.commit()
            await self.db.refresh(db_brand)
        except IntegrityError as e:
            await self.db.rollback()
            if isinstance(e.orig, UniqueViolation):
                raise DuplicateError('Brand already exists')
            raise DatabaseException('DB error')

        return db_brand

    async def list_brand(self) -> list[BrandDB]:
        query = select(BrandDB).where(BrandDB.is_active.is_(True))

        result = await self.db.execute(query)

        brands = result.scalars().all()

        return list(brands)

    async def get_brand_by_id(self, brand_id: int) -> BrandDB:
        brand_query = select(BrandDB).where(BrandDB.id == brand_id)
        brand_result = await self.db.execute(brand_query)
        brand = brand_result.scalar_one_or_none()

        if not brand:
            raise DatabaseException('This brand doesn\'t exist')

        return brand


class BrandReassignRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def reassign_brand(self, brand_id: int, subcompany_id: int) -> BrandDB:
        updated_brand = await self._update_brand_subcompany(brand_id, subcompany_id)
        await self._add_brand_subcompany_reassign_history(brand_id, subcompany_id)

        await self.db.commit()

        return updated_brand

    async def _update_brand_subcompany(self, brand_id: int, subcompany_id: int) -> BrandDB:
        stmt = (
            update(BrandDB)
            .where(BrandDB.id == brand_id)
            .values(subcompany_id=subcompany_id)
            .returning(BrandDB)
        )
        result = await self.db.execute(stmt)
        updated_brand = result.scalar_one()

        return updated_brand

    async def _add_brand_subcompany_reassign_history(self, brand_id: int, subcompany_id: int) -> None:
        stmt = insert(subcompany_brand_association_history).values(
            subcompany_id=subcompany_id,
            brand_id=brand_id
        )

        await self.db.execute(stmt)
