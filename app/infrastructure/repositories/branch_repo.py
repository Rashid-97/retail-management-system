from psycopg.errors import UniqueViolation
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import DuplicateError, DatabaseException
from app.domain.entities.entity import Branch
from app.domain.repositories.branch import IBranchRepository
from app.infrastructure.database.models.branch import BranchDB


class BranchRepository(IBranchRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_branch(self, branch: Branch) -> BranchDB:
        db_branch = BranchDB(**vars(branch))
        try:
            self.db.add(db_branch)
            await self.db.commit()
            await self.db.refresh(db_branch)
        except IntegrityError as e:
            await self.db.rollback()
            if isinstance(e.orig, UniqueViolation):
                raise DuplicateError('Branch already exists')
            raise DatabaseException('DB error')

        return db_branch

    async def list_branch(self) -> list[BranchDB]:
        query = select(BranchDB).where(BranchDB.is_active.is_(True))

        result = await self.db.execute(query)

        branches = result.scalars().all()

        return list(branches)