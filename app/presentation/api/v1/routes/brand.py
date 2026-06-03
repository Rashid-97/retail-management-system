from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.services.brand import BrandReassignService
from app.application.use_cases.brand import CreateBrandUseCase, ListBrandUseCase, ReassignBrandUseCase
from app.domain.entities.entity import Brand
from app.infrastructure.database.database import get_db
from app.infrastructure.repositories.brand_repo import BrandRepository, BrandReassignRepository
from app.presentation.api.v1.schemas.brand import BrandCreateModel, BrandReassignModel

router = APIRouter(
    prefix="/brand",
    tags=["Brand"]
)

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_brand(brand_data: BrandCreateModel, db: AsyncSession = Depends(get_db)):
    product = Brand(**brand_data.model_dump())
    product_repo = BrandRepository(db)
    use_case = CreateBrandUseCase(product_repo)
    new_product = await use_case.execute(product)
    return {'data': new_product.to_dict()}


@router.get("/list")
async def list_brands(db: AsyncSession = Depends(get_db)):
    list_brand_repo = BrandRepository(db)
    use_case = ListBrandUseCase(list_brand_repo)
    brand_list = await use_case.execute()
    return {'data': brand_list}


@router.post("/reassign")
async def reassign_brand(data: BrandReassignModel, db: AsyncSession = Depends(get_db)):
    brand_repo = BrandRepository(db)
    brand_reassign_repo = BrandReassignRepository(db)
    brand_reassign_service = BrandReassignService(
        brand_reassign_repo,
        brand_repo
    )
    use_case = ReassignBrandUseCase(brand_reassign_service)
    reassigned_brand = await use_case.execute(data.brand_id, data.subcompany_id)
    return {'data': reassigned_brand}
