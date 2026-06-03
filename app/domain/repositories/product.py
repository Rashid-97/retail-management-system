from abc import ABC, abstractmethod

from app.domain.entities.entity import Product, ProductCategory, ProductAssortment


class IProductRepository(ABC):
    @abstractmethod
    async def create_product(self, product: Product):
        pass

    @abstractmethod
    async def list_product(self):
        pass

    @abstractmethod
    async def detail_product(self, id: int):
        pass


class IProductCategoryRepository(ABC):
    @abstractmethod
    async def create_product_category(self, product_category: ProductCategory):
        pass

    @abstractmethod
    async def list_product_category(self):
        pass


class IProductAssortmentRepository(ABC):
    @abstractmethod
    async def save_assortment(self, assortment: ProductAssortment):
        pass

    @abstractmethod
    async def list_assortment(self):
        pass
