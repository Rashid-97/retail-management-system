from abc import ABC, abstractmethod

from app.infrastructure.database.models.stock import StockDB


class IStockRepository(ABC):
    @abstractmethod
    def list_stock(self) -> list[StockDB]:
        pass

    @abstractmethod
    def detail_stock(self, id: int) -> StockDB:
        pass

    @abstractmethod
    def get_stock_by_filters(self, filters: dict) -> StockDB:
        pass

    @abstractmethod
    def decrease_stock(self, id: int, quantity: int) -> StockDB:
        pass
