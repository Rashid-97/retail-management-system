from datetime import datetime

from sqlalchemy import Integer, ForeignKey, DateTime, Numeric, func
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class SalesDB(Base):
    __tablename__ = "sales"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    branch_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("branches.id"),
        nullable=False
    )

    product_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    date_time: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    discounted_selling_price: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    discounted_percentage: Mapped[float] = mapped_column(
        Numeric(5, 2),
        nullable=False
    )

    employee_id: Mapped[int] = mapped_column(Integer, nullable=False)

    customer_id: Mapped[int] = mapped_column(Integer, nullable=False)