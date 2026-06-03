from app.domain.entities.entity import Branch
from app.domain.repositories.branch import IBranchRepository
from app.infrastructure.database.models.branch import BranchDB


class CreateBranchUseCase:
    def __init__(self, repo : IBranchRepository):
        self.repo = repo

    async def execute(self, brand: Branch) -> BranchDB:
        new_branch = await self.repo.create_branch(brand)
        return new_branch

class ListBranchUseCase:
    def __init__(self, repo : IBranchRepository):
        self.repo = repo

    async def execute(self) -> list[BranchDB]:
        list_branch = await self.repo.list_branch()
        return list_branch