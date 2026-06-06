from app.application.services.product import CreateProductAssortmentMediator
from app.domain.entities.entity import Product, ProductCategory, ProductAssortment
from app.domain.repositories.branch import IBranchRepository
from app.domain.repositories.product import IProductRepository, IProductCategoryRepository, IProductAssortmentRepository
from app.infrastructure.database.models.product import ProductDB, ProductCategoryDB, ProductAssortmentDB
from app.infrastructure.repositories.product_repo import ProductAssortmentRepository


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


class CreateProductAssortmentUseCase:
    def __init__(self, product_assortment_mediator : CreateProductAssortmentMediator):
        self.product_assortment_mediator = product_assortment_mediator

    async def execute(self, product_assortment: ProductAssortment) -> ProductAssortmentDB:
        return await self.product_assortment_mediator.save_assortment(product_assortment)
