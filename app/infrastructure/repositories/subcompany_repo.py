from psycopg.errors import UniqueViolation
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import DuplicateError, DatabaseException
from app.domain.entities.entity import SubCompany
from app.domain.repositories.subcompany import ISubCompanyRepository
from app.infrastructure.database.models.brand import BrandDB
from app.infrastructure.database.models.subcompany import SubCompanyDB


class SubCompanyRepository(ISubCompanyRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_subcompany(self, subcompany: SubCompany) -> SubCompanyDB:
        data = vars(subcompany).copy()

        data.pop("brands_list")

        db_subcompany = SubCompanyDB(
            **data
        )

        try:
            self.db.add(db_subcompany)
            await self.db.commit()
            await self.db.refresh(db_subcompany)
        except IntegrityError as e:
            await self.db.rollback()
            if isinstance(e.orig, UniqueViolation):
                raise DuplicateError('Sub Company already exists')
            raise DatabaseException('DB error')

        return db_subcompany

    async def list_subcompany(self) -> list[SubCompanyDB]:
        query = select(SubCompanyDB).where(SubCompanyDB.is_active.is_(True))

        result = await self.db.execute(query)

        subcompanies = result.scalars().all()

        return list(subcompanies)