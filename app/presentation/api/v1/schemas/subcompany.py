from pydantic import BaseModel


class SubCompanyCreateModel(BaseModel):
    name: str
    is_active: bool = True
