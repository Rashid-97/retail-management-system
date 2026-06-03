from sqlalchemy import (
    String,
    Integer,
    Boolean, ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.infrastructure.database.base import Base
from app.infrastructure.database.models.brand import BrandDB


class BranchDB(Base):

    __tablename__ = "branches"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    brand_id: Mapped[int] = mapped_column(
        ForeignKey(BrandDB.id),
    )

    name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    address: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )
