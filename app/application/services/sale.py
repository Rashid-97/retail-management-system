from app.application.services.service import product_branch_brands_are_same
from app.core.exceptions import DomainValidationError, NotFoundException
from app.domain.entities.entity import Sale, Stock
from app.domain.repositories.branch import IBranchRepository
from app.domain.repositories.product import IProductRepository
from app.domain.repositories.sale import ISaleRepository
from app.domain.repositories.stock import IStockRepository


class SaleMediator:
    def __init__(self, product_repository : IProductRepository,
                 branch_repo: IBranchRepository,
                 stock_repo: IStockRepository,
                 sale_repo: ISaleRepository):
        self.product_repository = product_repository
        self.branch_repo = branch_repo
        self.stock_repo = stock_repo
        self.sale_repo = sale_repo

    async def create_sale(self, sale: Sale):
        product = await self.product_repository.detail_product(sale.product_id)
        branch = await self.branch_repo.detail_branch(sale.branch_id)

        if not product:
            raise NotFoundException('Product not found')
        if not branch:
            raise NotFoundException('Branch not found')

        self._check_product_branch_brands_are_same(product.brand_id, branch.brand_id)

        stock = await self.stock_repo.get_stock_by_filters({
            'product_id': product.id,
            'branch_id': branch.id,
        })
        self._check_product_exists_in_stock(sale.quantity, stock.quantity)
        await self.stock_repo.decrease_stock(stock.id, sale.quantity)
        return await self.sale_repo.create(sale)

    def _check_product_branch_brands_are_same(self, product_brand_id: int, branch_brand_id: int) -> bool:
        if not product_branch_brands_are_same(product_brand_id, branch_brand_id):
            raise DomainValidationError('Product\'s brand is not same with branch\'s')
        return True

    def _check_product_exists_in_stock(self, sale_product_quantity: int, stock_quantity: int) -> bool:
        if sale_product_quantity > stock_quantity:
            raise DomainValidationError('Product quantity cannot be greater than stock quantity')
        return True
