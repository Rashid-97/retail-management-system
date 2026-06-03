from sqlalchemy import (
    String,
    Integer,
    Boolean
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)

from app.infrastructure.database.base import Base


class SubCompanyDB(Base):

    __tablename__ = "subcompanies"


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

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    brands = relationship("BrandDB", back_populates="subcompany")
