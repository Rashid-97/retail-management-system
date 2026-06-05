from fastapi import APIRouter

from app.domain.entities.entity import Sale
from app.infrastructure.services.db_management import SqlAlchemyFacade as DbFacade
from app.presentation.api.v1.schemas.sale import SaleCreateModel

router = APIRouter(
    prefix="/sale",
    tags=["Sale"]
)

@router.post("/create")
def create_sale(data: SaleCreateModel):
    # sale = Sale(**data.model_dump())
    # repo = SaleRepository(DbFacade())
    # use_case = CreateSaleUseCase(repo)
    # sale_result = await use_case.execute(sale)
    pass