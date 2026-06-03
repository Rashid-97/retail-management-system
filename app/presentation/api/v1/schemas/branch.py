from pydantic import BaseModel


class BranchCreateModel(BaseModel):
    brand_id: int
    name: str
    address: str
    is_active: bool = True
