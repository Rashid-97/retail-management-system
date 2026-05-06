from __future__ import annotations

from datetime import datetime


class Store:
    pass

class Brand:
    def __init__(self, id: int, name: str, is_active: bool):
        self.id = id
        self.name = name
        self.is_active = is_active

class SubCompany:
    def __init__(self, id: int, name: str, brands_list: list[Brand], is_active: bool):
        self.id = id
        self.name = name
        self.brands_list = brands_list
        self.is_active = is_active

class Branch:
    def __int__(self, id: int, brand_id: int, name: str, address: str, is_active: bool):
        self.id = id
        self.brand_id = brand_id
        self.name = name
        self.address = address
        self.is_active = is_active

class Product:
    def __init__(self, id: int, name: str, brand_id: int, category: int, purchase_price: float,
                 base_selling_price: float, color: str, size: int, is_active: bool):
        self.id = id
        self.name = name
        self.brand_id = brand_id
        self.category = category
        self.purchase_price = purchase_price
        self.base_selling_price = base_selling_price
        self.color = color
        self.size = size
        self.is_active = is_active

class ProductCategory:
    pass

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
    def __init__(self, sale_id: int, branch_id: int, product_id: int, quantity: int, date_time: datetime,
                 discounted_selling_price: float, discounted_percentage: float, employee_id: int, customer_id: int):
        self.sale_id = sale_id
        self.branch_id = branch_id
        self.product_id = product_id
        self.quantity = quantity
        self.date_time = date_time
        self.discounted_selling_price = discounted_selling_price
        self.discounted_percentage = discounted_percentage
        self.employee_id = employee_id
        self.customer_id = customer_id

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
