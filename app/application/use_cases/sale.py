from app.domain.entities.entity import Sale
from app.domain.repositories.sale import ISaleRepository


class CreateSaleUseCase:
    def __init__(self, repo: ISaleRepository):
        self.repo = repo

    async def execute(self, sale: Sale):
        # business logic check
        self.repo.create(sale)
