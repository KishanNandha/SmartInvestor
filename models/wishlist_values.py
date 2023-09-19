# app/models/wishlist_values.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class WishlistValue(Base):
    __tablename__ = "wishlist_values"
    value_id = Column(Integer, primary_key=True, index=True)
    wishlist_id = Column(Integer, ForeignKey('wishlists.wishlist_id'))
    string_value = Column(String(length=255))

    wishlist = relationship("Wishlist", back_populates="wishlist_value")
