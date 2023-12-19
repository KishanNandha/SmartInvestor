# app/controllers/wishlist_controller.py
from fastapi import HTTPException
import yfinance as yf
from datetime import datetime
import json

def getTickerTimeSeries(symbol: str, start_date: str, end_date: str):
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    try:
        # Create Ticker object for the specified symbol
        ticker = yf.Ticker(symbol)

        # Download daily historical data for the specified time period
        hist = ticker.history(start=start_date, end=end_date, interval="1d")

        # Filter and select the desired columns
        selected_columns = ["Open", "High", "Low", "Close"]
        # Reset index and convert the date column to a string
        filtered_data = hist[selected_columns].reset_index()
        filtered_data['Date'] = filtered_data['Date'].dt.strftime('%Y-%m-%d')

        # Convert the DataFrame to a dictionary
        timeseries_dict = filtered_data.to_dict(orient='records')

        # Convert the dictionary to a JSON object with pretty printing
        timeseries_json = json.dumps(timeseries_dict, indent=2)

        return json.loads(timeseries_json)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")