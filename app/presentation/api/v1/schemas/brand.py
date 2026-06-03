from pydantic import BaseModel


class BrandCreateModel(BaseModel):
    name: str
    subcompany_id: int
    is_active: bool = True


class BrandReassignModel(BaseModel):
    brand_id: int
    subcompany_id: int
