from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.use_cases.subcompany import CreateSubCompanyUseCase
from app.domain.entities.entity import SubCompany
from app.infrastructure.database.database import get_db
from app.infrastructure.repositories.subcompany_repo import SubCompanyRepository
from app.presentation.api.v1.schemas.subcompany import SubCompanyCreateModel

router = APIRouter(
    prefix="/subcompany",
    tags=["Subcompany"]
)

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_subcompany(subcompany_data: SubCompanyCreateModel, db: AsyncSession = Depends(get_db)):
    subcompany = SubCompany(**subcompany_data.model_dump())
    subcompany_repo = SubCompanyRepository(db)
    use_case = CreateSubCompanyUseCase(subcompany_repo)
    new_subcompany = await use_case.execute(subcompany)
    return {'data': new_subcompany.to_dict()}
