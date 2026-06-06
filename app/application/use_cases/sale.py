from app.application.services.sale import SaleMediator
from app.core.exceptions import DomainValidationError
from app.domain.entities.entity import Sale


class CreateSaleUseCase:
    def __init__(self, sale_mediator: SaleMediator):
        self.sale_mediator = sale_mediator

    async def execute(self, sale: Sale):
        if sale.quantity < 1:
            raise DomainValidationError('Quantity should be greater than 1')
        return await self.sale_mediator.create_sale(sale)
