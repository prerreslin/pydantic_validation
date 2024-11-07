from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .. import Base

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    product_name: Mapped[str] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(default=1)
    price_per_unit: Mapped[float]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship("User", back_populates="orders")