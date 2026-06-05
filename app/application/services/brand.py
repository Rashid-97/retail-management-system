from __future__ import annotations

from app.core.exceptions import DomainValidationError
from app.infrastructure.repositories.brand_repo import BrandReassignRepository, BrandRepository


class BrandReassignService:
    def __init__(self, brand_mediator: BrandMediator):
        self.brand_mediator = brand_mediator

    async def assign(self, brand_id: int, subcompany_id: int):
        return await self.brand_mediator.reassign(brand_id, subcompany_id)


class BrandMediator:
    def __init__(self, brand_reassign_repo: BrandReassignRepository,
                 brand_repo: BrandRepository):
        self.brand_reassign_repo = brand_reassign_repo
        self.brand_repo = brand_repo

    async def reassign(self, brand_id: int, subcompany_id: int):
        brand = await self.brand_repo.get_brand_by_id(brand_id)
        await self._check_brand_subcompany_relation(subcompany_id, brand.subcompany_id)

        return await self.brand_reassign_repo.reassign_brand(brand_id, subcompany_id)

    async def _check_brand_subcompany_relation(self, subcompany_id: int, brand_subcompany_id: int):
        if subcompany_id == brand_subcompany_id:
            raise DomainValidationError('This brand is already assigned to this subcompany')
