from sqlalchemy.orm import Mapped,relationship,mapped_column
from .. import Base

class User(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    orders: Mapped[list["Order"]] = relationship("Order", back_populates="user")