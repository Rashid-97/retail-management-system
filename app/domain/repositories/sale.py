from abc import ABC, abstractmethod

from app.domain.entities.entity import Sale


class ISaleRepository(ABC):
    @abstractmethod
    async def create(self, data: Sale):
        pass
