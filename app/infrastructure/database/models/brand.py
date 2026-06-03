from sqlalchemy import (
    String,
    Integer,
    Boolean, ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)

from app.infrastructure.database.base import Base


class BrandDB(Base):

    __tablename__ = "brands"


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

    subcompany_id: Mapped[int] = mapped_column(
        ForeignKey("subcompanies.id")
    )

    subcompany = relationship(
        "SubCompanyDB",
        back_populates="brands"
    )
