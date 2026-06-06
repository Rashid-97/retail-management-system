from pydantic import BaseModel


class SaleCreateModel(BaseModel):
    branch_id: int
    product_id: int
    quantity: int
    discounted_selling_price: float
    discounted_percentage: int
    employee_id: int
    customer_id: int
