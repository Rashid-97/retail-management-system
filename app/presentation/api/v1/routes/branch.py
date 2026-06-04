from fastapi import APIRouter, status

from app.application.use_cases.branch import CreateBranchUseCase
from app.domain.entities.entity import Branch
from app.infrastructure.repositories.branch_repo import BranchRepository
from app.infrastructure.services.db_management import SqlAlchemyFacade as DbFacade
from app.presentation.api.v1.schemas.branch import BranchCreateModel

router = APIRouter(
    prefix="/branch",
    tags=["Branch"]
)

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_branch(branch_data: BranchCreateModel):
    branch = Branch(**branch_data.model_dump())
    branch_repo = BranchRepository(DbFacade())
    use_case = CreateBranchUseCase(branch_repo)
    new_branch = await use_case.execute(branch)
    return {'data': new_branch.to_dict()}
