from . import product, brand, branch, subcompany

"""
    collecting routers for importing them to FastApi app in main.py
"""
routers = [
    product.router,
    brand.router,
    branch.router,
    subcompany.router
]