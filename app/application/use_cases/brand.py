from app.application.services.brand import BrandReassignService
from app.domain.entities.entity import Brand
from app.domain.repositories.brand import IBrandRepository
from app.infrastructure.database.models.brand import BrandDB
from app.infrastructure.repositories.brand_repo import BrandReassignRepository


class CreateBrandUseCase:
    def __init__(self, repo : IBrandRepository):
        self.repo = repo

    async def execute(self, brand: Brand) -> BrandDB:
        new_brand = await self.repo.create_brand(brand)
        return new_brand

class ListBrandUseCase:
    def __init__(self, repo : IBrandRepository):
        self.repo = repo

    async def execute(self) -> list[BrandDB]:
        list_brand = await self.repo.list_brand()
        return list_brand


class ReassignBrandUseCase:
    def __init__(self, brand_reassign_service : BrandReassignService):
        self.brand_reassign_service = brand_reassign_service

    async def execute(self, brand_id: int, subcompany_id: int) -> BrandDB:
        data = await self.brand_reassign_service.assign(brand_id, subcompany_id)

        return data
