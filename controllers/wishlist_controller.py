# app/controllers/wishlist_controller.py
from sqlalchemy.orm import Session
from app.models.wishlist import Wishlist
from app.schemas import WishlistCreate


def create_wishlist(db: Session, wishlist: WishlistCreate):
    db_wishlist = Wishlist(**wishlist.dict())
    db.add(db_wishlist)
    db.commit()
    db.refresh(db_wishlist)
    return db_wishlist


def get_wishlist(db: Session, wishlist_id: int):
    return db.query(Wishlist).filter(Wishlist.wishlist_id == wishlist_id).first()


def get_wishlists(db: Session):
    return db.query(Wishlist).all()
