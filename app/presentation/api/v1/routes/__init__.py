from . import product, brand, branch, subcompany, stock, sale

"""
    collecting routers for importing them to FastApi app in main.py
"""
routers = [
    product.router,
    brand.router,
    branch.router,
    subcompany.router,
    stock.router,
    sale.router
]