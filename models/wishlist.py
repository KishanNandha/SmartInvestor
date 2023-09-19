# app/models/wishlist.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base


class Wishlist(Base):
    __tablename__ = "wishlists"
    wishlist_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(length=255), index=True)

    wishlist_value = relationship("WishlistValue", back_populates="wishlist")


