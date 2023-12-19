# app/main.py
from fastapi import FastAPI
from routes import ticker_details_routes

app = FastAPI()

app.include_router(ticker_details_routes.router)

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to SmartInvestor"}

@app.get('/test')
def test():
    return {"message": "Welcome to SmartInvestor"}