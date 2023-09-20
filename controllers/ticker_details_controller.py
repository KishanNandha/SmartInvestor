# app/controllers/wishlist_controller.py
from sqlalchemy.orm import Session
from service.FA.ticker_financials_service import get_ticker_financials, get_ticker_price_data


def get_ticker_details_controller(db: Session, ticker_name: str):
    financials = get_ticker_financials(ticker_name)
    price_data = get_ticker_price_data(ticker_name)
    ticker_details = {
        "priceData": price_data,
        "financials": financials,
        "technicals": {}
    }

    return ticker_details
