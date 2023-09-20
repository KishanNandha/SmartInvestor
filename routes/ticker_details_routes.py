# routes/wishlist_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import init_db
from controllers.ticker_details_controller import get_ticker_details_controller

router = APIRouter()

@router.get("/ticker/details/{ticker_name}")
def get_ticker_details(ticker_name: str, db: Session = Depends(init_db)):
    ticker_details = get_ticker_details_controller(db, ticker_name)
    return ticker_details
