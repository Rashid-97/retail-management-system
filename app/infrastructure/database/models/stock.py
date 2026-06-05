from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base
from app.infrastructure.database.models import ProductDB, BranchDB


class StockDB(Base):

    __tablename__ = "stocks"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    branch_id: Mapped[int] = mapped_column(
        ForeignKey(BranchDB.id),
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey(ProductDB.id),
    )

    quantity: Mapped[int] = mapped_column(
        Integer
    )
