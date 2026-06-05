from app.domain.repositories.stock import IStockRepository
from app.infrastructure.database.models.stock import StockDB
from app.infrastructure.services.db_management import DatabaseFacade


class StockRepository(IStockRepository):
    def __init__(self, db_facade: DatabaseFacade):
        self.db_facade = db_facade

    async def list_stock(self) -> list[StockDB]:
        return await self.db_facade.list(StockDB)