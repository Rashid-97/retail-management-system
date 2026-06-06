from pydantic import BaseModel


class ProductCreateModel(BaseModel):
    name: str
    brand_id: int
    category: int
    purchase_price: float
    base_selling_price: float
    color: str
    size: int
    is_active: bool = True


class ProductCategoryCreateModel(BaseModel):
    name: str


class ProductAssortmentCreateModel(BaseModel):
    product_id: int
    branch_id: int
    is_active: bool = True
