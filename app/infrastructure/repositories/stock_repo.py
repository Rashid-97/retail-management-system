from app.domain.repositories.stock import IStockRepository
from app.infrastructure.database.models.stock import StockDB
from app.infrastructure.services.db_management import DatabaseFacade


class StockRepository(IStockRepository):
    def __init__(self, db_facade: DatabaseFacade):
        self.db_facade = db_facade

    async def list_stock(self) -> list[StockDB]:
        return await self.db_facade.list(StockDB)

    async def detail_stock(self, id: int) -> StockDB:
        return await self.db_facade.get_by_id(StockDB, id)

    async def get_stock_by_filters(self, filters: dict) -> StockDB:
        return await self.db_facade.get_one(StockDB, filters)

    async def decrease_stock(self, id: int, quantity: int) -> StockDB:
        updated_stock = await self.db_facade.update(StockDB, id, {
            "quantity": getattr(StockDB, "quantity") - quantity
        })
        await self.db_facade.commit()
        return updated_stock
