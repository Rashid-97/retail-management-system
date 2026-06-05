from __future__ import annotations

from datetime import datetime

from app.core.exceptions import DomainValidationError


class Store:
    def __init__(self, brand_id: int):
        self.brand_id = brand_id

class Brand:
    def __init__(self, name: str, subcompany_id: int, is_active: bool, id: int = None):
        self.id = id
        self.name = name
        self.subcompany_id = subcompany_id
        self.is_active = is_active

class SubCompany:
    def __init__(self, name: str, is_active: bool, brands_list: list[Brand] = None, id: int = None):
        self.name = name
        self.is_active = is_active
        self.brands_list = brands_list
        self.id = id

class Branch:
    def __init__(self, brand_id: int, name: str, address: str, is_active: bool, id: int = None):
        self.brand_id = brand_id
        self.name = name
        self.address = address
        self.is_active = is_active
        self.id = id

class Product:
    def __init__(self, name: str, brand_id: int, category: int, purchase_price: float,
                 base_selling_price: float, color: str, size: int, is_active: bool, id: int = None):

        # Domain validations
        self._validate_name(name)
        self._validate_purchase_price(purchase_price)
        self._validate_base_selling_price(base_selling_price)
        # Initializing fields
        self.name = name
        self.brand_id = brand_id
        self.category = category
        self.purchase_price = purchase_price
        self.base_selling_price = base_selling_price
        self.color = color
        self.size = size
        self.is_active = is_active
        self.id = id

    def _validate_name(self, name: str) -> None | Exception:
        if len(name) < 2:
            raise DomainValidationError('Product name length should be greater than 2 characters')
        if len(name) > 50:
            raise DomainValidationError('Product name length should be less than 50 characters')
        return None

    def _validate_purchase_price(self, purchase_price: float) -> None | Exception:
        if purchase_price <= 0:
            raise DomainValidationError('Product purchase price should be greater than 0')
        return None

    def _validate_base_selling_price(self, base_selling_price: float) -> None | Exception:
        if base_selling_price <= 0:
            raise DomainValidationError('Product base selling price should be greater than 0')
        return None

class ProductCategory:
    def __init__(self, name: str, id: int = None):
        self.name = name
        self.id = id

class ProductAssortment:
    def __init__(self, branch_id: int, product_id: int, is_active: bool):
        self.branch_id = branch_id
        self.product_id = product_id
        self.is_active = is_active

class Stock:
    def __init__(self, branch_id: int, product_id: int, quantity: int):
        self.branch_id = branch_id
        self.product_id = product_id
        self.quantity = quantity

class Sales:
    def __init__(self, branch_id: int, product_id: int, quantity: int, date_time: datetime,
                 discounted_selling_price: float, discounted_percentage: float, employee_id: int, customer_id: int,
                 id: int = None):
        self.branch_id = branch_id
        self.product_id = product_id
        self.quantity = quantity
        self.date_time = date_time
        self.discounted_selling_price = discounted_selling_price
        self.discounted_percentage = discounted_percentage
        self.employee_id = employee_id
        self.customer_id = customer_id
        self.id = id

class Employee:
    pass

class JobPosition:
    pass

class Transfer:
    pass

class Payroll:
    pass

class Discount:
    def __init__(self, id: int, name: str, branch_list: list[Branch], product_list: list[Product],
                 discount_percentage: float,
                 start_date: datetime, end_date: datetime, is_active: bool, excluded_products: list[Product]):
        self.id = id
        self.name = name
        self.branch_list = branch_list
        self.product_list = product_list
        self.discount_percentage = discount_percentage
        self.start_date = start_date
        self.end_date = end_date
        self.is_active = is_active
        self.excluded_products = excluded_products

class Bonus:
    pass

class Sale:
    pass
