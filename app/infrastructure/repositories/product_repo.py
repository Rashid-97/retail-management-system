from app.domain.entities.entity import Product, ProductCategory, ProductAssortment
from app.domain.repositories.product import IProductRepository, IProductCategoryRepository, IProductAssortmentRepository
from app.infrastructure.database.models.product import ProductDB, ProductCategoryDB, ProductAssortmentDB
from app.infrastructure.services.db_management import DatabaseFacade


class ProductRepository(IProductRepository):
    def __init__(self, db_facade: DatabaseFacade):
        self.db_facade = db_facade

    async def create_product(self, product: Product) -> ProductDB:
        db_product = ProductDB(**vars(product))
        db_product = await self.db_facade.save(db_product)

        return db_product

    async def list_product(self) -> list[ProductDB]:
        return await self.db_facade.list_active(ProductDB)

    async def detail_product(self, id: int) -> ProductDB:
        return await self.db_facade.get_by_id(ProductDB, id)

class ProductCategoryRepository(IProductCategoryRepository):
    def __init__(self, db_facade: DatabaseFacade):
        self.db_facade = db_facade

    async def create_product_category(self, product_category: ProductCategory) -> ProductCategoryDB:
        db_product_category = ProductCategoryDB(**vars(product_category))
        db_product_category = await self.db_facade.save(db_product_category)

        return db_product_category

    async def list_product_category(self) -> list[ProductCategoryDB]:
        return await self.db_facade.list(ProductCategoryDB)


class ProductAssortmentRepository(IProductAssortmentRepository):
    def __init__(self, db_facade: DatabaseFacade):
        self.db_facade = db_facade

    async def save_assortment(self, product_assortment: ProductAssortment):
        db_product_assortment = ProductAssortmentDB(**vars(product_assortment))
        db_product_assortment = await self.db_facade.save(db_product_assortment)

        return db_product_assortment

    async def list_assortment(self) -> list[ProductAssortmentDB]:
        return await self.db_facade.list(ProductAssortmentDB)
