from fastapi import APIRouter

from app.application.services.sale import SaleMediator
from app.application.use_cases.sale import CreateSaleUseCase
from app.domain.entities.entity import Sale
from app.infrastructure.repositories.branch_repo import BranchRepository
from app.infrastructure.repositories.product_repo import ProductRepository
from app.infrastructure.repositories.sale_repo import SaleRepository
from app.infrastructure.repositories.stock_repo import StockRepository
from app.infrastructure.services.db_management import SqlAlchemyFacade as DbFacade
from app.presentation.api.v1.schemas.sale import SaleCreateModel

router = APIRouter(
    prefix="/sale",
    tags=["Sale"]
)

@router.post("/create")
async def create_sale(data: SaleCreateModel):
    sale = Sale(**data.model_dump())
    sale_repo = SaleRepository(DbFacade())
    product_repo = ProductRepository(DbFacade())
    branch_repo = BranchRepository(DbFacade())
    stock_repo = StockRepository(DbFacade())

    mediator = SaleMediator(
        product_repo,
        branch_repo,
        stock_repo,
        sale_repo
    )
    use_case = CreateSaleUseCase(mediator)
    sale_result = await use_case.execute(sale)
    return {'data': sale_result}