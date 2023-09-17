# app/controllers/wishlist_values_controller.py
from sqlalchemy.orm import Session
from app.models.wishlist_values import WishlistValue
from app.schemas import WishlistValueCreate


def create_wishlist_value(db: Session, wishlist_value: WishlistValueCreate):
    db_wishlist_value = WishlistValue(**wishlist_value.dict())
    db.add(db_wishlist_value)
    db.commit()
    db.refresh(db_wishlist_value)
    return db_wishlist_value


def get_wishlist_value(db: Session, value_id: int):
    return db.query(WishlistValue).filter(WishlistValue.value_id == value_id).first()


def get_wishlist_values(db: Session, wishlist_id: int):
    return db.query(WishlistValue).filter(WishlistValue.wishlist_id == wishlist_id).all()
