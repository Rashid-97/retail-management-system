from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime, func

from app.infrastructure.database.base import Base

"""
subcompany brand association history table
"""
subcompany_brand_association_history = Table(
    'subcompany_brand_association_history', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('subcompany_id', Integer, ForeignKey('subcompanies.id')),
    Column('brand_id', Integer, ForeignKey('brands.id')),
    Column('created_at', DateTime, server_default=func.now(), nullable=False)
)