from abc import ABC, abstractmethod

from app.domain.entities.entity import SubCompany


class ISubCompanyRepository(ABC):
    @abstractmethod
    async def create_subcompany(self, subcompany: SubCompany):
        pass

    @abstractmethod
    async def list_subcompany(self):
        pass