# app/models/wishlist.py
from sqlalchemy import Column, Integer, String
from app.database import Base


class Wishlist(Base):
    __tablename__ = 'wishlists'
    wishlist_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
