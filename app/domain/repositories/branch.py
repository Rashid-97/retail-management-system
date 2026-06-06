from abc import ABC, abstractmethod

from app.domain.entities.entity import Branch


class IBranchRepository(ABC):
    @abstractmethod
    async def create_branch(self, branch: Branch):
        pass

    @abstractmethod
    async def list_branch(self):
        pass

    @abstractmethod
    async def detail_branch(self, id: int):
        pass