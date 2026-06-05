from abc import ABC, abstractmethod

from app.infrastructure.database.models.stock import StockDB


class IStockRepository(ABC):
    @abstractmethod
    def list_stock(self) -> list[StockDB]:
        pass