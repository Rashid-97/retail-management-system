from app.application.services.service import product_branch_brands_are_same
from app.core.exceptions import DomainValidationError, DatabaseException, NotFoundException
from app.domain.entities.entity import ProductAssortment
from app.domain.repositories.branch import IBranchRepository
from app.domain.repositories.product import IProductAssortmentRepository, IProductRepository


class CreateProductAssortmentMediator:
    def __init__(self, product_assortment_repo : IProductAssortmentRepository,
                 product_repository : IProductRepository,
                 branch_repo: IBranchRepository):
        self.product_assortment_repo = product_assortment_repo
        self.product_repository = product_repository
        self.branch_repo = branch_repo

    async def save_assortment(self, product_assortment: ProductAssortment):
        product = await self.product_repository.detail_product(product_assortment.product_id)
        branch = await self.branch_repo.detail_branch(product_assortment.branch_id)

        if not product:
            raise NotFoundException('Product not found')
        if not branch:
            raise NotFoundException('Branch not found')

        self._check_product_branch_brands_are_same(product.brand_id, branch.brand_id)

        return await self.product_assortment_repo.save_assortment(product_assortment)

    def _check_product_branch_brands_are_same(self, product_brand_id: int, branch_brand_id: int) -> bool:
        if not product_branch_brands_are_same(product_brand_id, branch_brand_id):
            raise DomainValidationError('Product brand is not same with branch\'s')
        return True
