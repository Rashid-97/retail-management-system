from app.domain.entities.entity import SubCompany
from app.domain.repositories.subcompany import ISubCompanyRepository
from app.infrastructure.database.models.subcompany import SubCompanyDB


class CreateSubCompanyUseCase:
    def __init__(self, repo : ISubCompanyRepository):
        self.repo = repo

    async def execute(self, subcompany: SubCompany) -> SubCompanyDB:
        new_subcompany = await self.repo.create_subcompany(subcompany)
        return new_subcompany

class ListSubCompanyUseCase:
    def __init__(self, repo : ISubCompanyRepository):
        self.repo = repo

    async def execute(self) -> list[SubCompanyDB]:
        list_subcompany = await self.repo.list_subcompany()
        return list_subcompany