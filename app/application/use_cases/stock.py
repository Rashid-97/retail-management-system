from app.infrastructure.repositories.stock_repo import StockRepository


class ListStockUseCase:
    def __init__(self, repo: StockRepository):
        self.repo = repo

    async def execute(self):
        return await self.repo.list_stock()
