from psycopg.errors import UniqueViolation
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import DuplicateError, DatabaseException
from app.domain.entities.entity import Branch
from app.domain.repositories.branch import IBranchRepository
from app.infrastructure.database.models.branch import BranchDB
from app.infrastructure.services.db_management import DatabaseFacade


class BranchRepository(IBranchRepository):
    def __init__(self, db_facade: DatabaseFacade):
        self.db_facade = db_facade

    async def create_branch(self, branch: Branch) -> BranchDB:
        return await self.db_facade.save(BranchDB(**vars(branch)))

    async def list_branch(self) -> list[BranchDB]:
        return await self.db_facade.list_active(BranchDB)
