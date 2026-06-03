from app.domain.entities.entity import Product, ProductCategory
from app.domain.repositories.product import IProductRepository, IProductCategoryRepository, IProductAssortmentRepository
from app.infrastructure.database.models.product import ProductDB, ProductCategoryDB, ProductAssortmentDB


class CreateProductUseCase:
    def __init__(self, repo : IProductRepository):
        self.repo = repo

    async def execute(self, product: Product) -> ProductDB:
        new_product = await self.repo.create_product(product)
        return new_product


class ListProductUseCase:
    def __init__(self, repo : IProductRepository):
        self.repo = repo

    async def execute(self) -> ProductDB:
        list_product = await self.repo.list_product()
        return list_product


class DetailProductUseCase:
    def __init__(self, repo : IProductRepository):
        self.repo = repo

    async def execute(self, id: int) -> ProductDB:
        detail_product = await self.repo.detail_product(id)
        return detail_product


class CreateProductCategoryUseCase:
    def __init__(self, repo : IProductCategoryRepository):
        self.repo = repo

    async def execute(self, product_category: ProductCategory) -> ProductCategoryDB:
        new_product_category = await self.repo.create_product_category(product_category)
        return new_product_category


class ListProductCategoryUseCase:
    def __init__(self, repo : IProductCategoryRepository):
        self.repo = repo

    async def execute(self) -> ProductCategoryDB:
        list_product_category = await self.repo.list_product_category()
        return list_product_category


class ListProductAssortmentUseCase:
    def __init__(self, repo : IProductAssortmentRepository):
        self.repo = repo

    async def execute(self) -> ProductAssortmentDB:
        list_product_assortment = await self.repo.list_assortment()
        return list_product_assortment
