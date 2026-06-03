from sqlalchemy import (
    String,
    Integer,
    Numeric,
    Boolean, ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.infrastructure.database.base import Base
from app.infrastructure.database.models.brand import BrandDB


class ProductDB(Base):

    __tablename__ = "products"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    brand_id: Mapped[int] = mapped_column(
        ForeignKey(BrandDB.id),
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        ForeignKey("product_category.id"),
        nullable=False
    )

    purchase_price: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    base_selling_price: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    color: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    size: Mapped[str] = mapped_column(
        Integer,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )


class ProductCategoryDB(Base):

    __tablename__ = "product_category"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )


class ProductAssortmentDB(Base):

    __tablename__ = "product_assortments"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    branch_id: Mapped[int] = mapped_column(
        ForeignKey("branches.id")
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id")
    )

