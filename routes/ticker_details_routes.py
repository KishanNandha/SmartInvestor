# routes/wishlist_routes.py
from fastapi import APIRouter, Depends

from controllers.ticker_details_controller import getTickerTimeSeries

router = APIRouter()

@router.get("/si/ticker/timeseries/{symbol}/{start_date}/{end_date}")
def get_ticker_details(symbol: str, start_date: str, end_date: str):

    return getTickerTimeSeries(symbol, start_date, end_date)
