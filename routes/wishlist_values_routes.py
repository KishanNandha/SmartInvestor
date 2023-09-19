# app/routes/wishlist_values_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import init_db
from controllers.wishlist_values_controller import (
    create_wishlist_value, get_wishlist_value, get_wishlist_values
)
from schemas.wishlist_values import WishlistValueCreate, WishlistValueOut
from typing import List

router = APIRouter()


@router.post("/wishlist_values/", response_model=WishlistValueOut)
def create_new_wishlist_value(value: WishlistValueCreate, db: Session = Depends(init_db)):
    return create_wishlist_value(db, value)


@router.get("/wishlist_values/{value_id}/", response_model=WishlistValueOut)
def read_wishlist_value(value_id: int, db: Session = Depends(init_db)):
    db_wishlist_value = get_wishlist_value(db, value_id)
    if db_wishlist_value is None:
        raise HTTPException(status_code=404, detail="Wishlist Value not found")
    return db_wishlist_value


@router.get("/wishlist_values/wishlist/{wishlist_id}/", response_model=List[WishlistValueOut])
def read_wishlist_values(wishlist_id: int, db: Session = Depends(init_db)):
    wishlist_values = get_wishlist_values(db, wishlist_id)
    return wishlist_values
