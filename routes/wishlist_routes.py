# app/routes/wishlist_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers.wishlist_controller import create_wishlist, get_wishlist, get_wishlists
from app.schemas import WishlistCreate, WishlistOut

router = APIRouter()


@router.post("/wishlist/", response_model=WishlistOut)
def create_new_wishlist(wishlist: WishlistCreate, db: Session = Depends(get_db)):
    return create_wishlist(db, wishlist)


@router.get("/wishlist/{wishlist_id}/", response_model=WishlistOut)
def read_wishlist(wishlist_id: int, db: Session = Depends(get_db)):
    db_wishlist = get_wishlist(db, wishlist_id)
    if db_wishlist is None:
        raise HTTPException(status_code=404, detail="Wishlist not found")
    return db_wishlist


@router.get("/wishlists/", response_model=list[WishlistOut])
def read_wishlists(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    wishlists = get_wishlists(db)
    return wishlists[skip:skip + limit]
