from app.domain.entities.entity import Sale
from app.domain.repositories.sale import ISaleRepository
from app.infrastructure.database.models import SalesDB
from app.infrastructure.services.db_management import DatabaseFacade


class SaleRepository(ISaleRepository):
    def __init__(self, db_facade: DatabaseFacade):
        self.db_facade = db_facade

    async def create(self, sale: Sale):
        return await self.db_facade.save(SalesDB(**vars(sale)))
