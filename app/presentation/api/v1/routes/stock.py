from fastapi import APIRouter

from app.application.use_cases.stock import ListStockUseCase
from app.infrastructure.repositories.stock_repo import StockRepository
from app.infrastructure.services.db_management import SqlAlchemyFacade as DbFacade

router = APIRouter(
    prefix="/stock",
    tags=["Stock"]
)

@router.get("/list")
async def get_stock():
    stock_repo = StockRepository(DbFacade())
    use_case = ListStockUseCase(stock_repo)
    stocks = await use_case.execute()
    return {'data': stocks}