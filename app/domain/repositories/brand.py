from abc import ABC, abstractmethod

from app.domain.entities.entity import Brand


class IBrandRepository(ABC):
    @abstractmethod
    async def create_brand(self, brand: Brand):
        pass

    @abstractmethod
    async def list_brand(self):
        pass

    @abstractmethod
    async def get_brand_by_id(self, brand_id: int):
        pass
