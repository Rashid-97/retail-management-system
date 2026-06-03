from sqlalchemy import Table, Column, Integer, Boolean, ForeignKey, UniqueConstraint

from app.infrastructure.database.base import Base

"""
subcompany brand association history table
"""
subcompany_brand_association_history = Table(
    'subcompany_brand_association_history', Base.metadata,
    Column('subcompany_id', Integer, ForeignKey('subcompanies.id'), primary_key=True),
    Column('brand_id', Integer, ForeignKey('brands.id'), primary_key=True),
    UniqueConstraint('brand_id', 'subcompany_id', name='uq_brand_status_subcompany_history')
)