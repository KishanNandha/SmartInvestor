from yahoofinancials import YahooFinancials


def get_ticker_price_data(ticker: str):
    yahoo_financials = YahooFinancials(ticker)
    stock_data = yahoo_financials.get_stock_price_data(reformat=True)
    return stock_data

def get_ticker_financials(ticker: str):
    yahoo_financials = YahooFinancials(ticker)
    stock_data = yahoo_financials.get_financial_data()

    financials = {
            "ebitda": stock_data.get("ebitda"),
            "totalDebt": stock_data.get("totalDebt"),
            "quickRatio": stock_data.get("quickRatio"),
            "currentRatio": stock_data.get("currentRatio"),
            "totalRevenue": stock_data.get("totalRevenue"),
            "debtToEquity": stock_data.get("debtToEquity"),
            "revenuePerShare": stock_data.get("revenuePerShare"),
            "returnOnAssets": stock_data.get("returnOnAssets"),
            "returnOnEquity": stock_data.get("returnOnEquity")
        }
    return stock_data
