# app/main.py
from fastapi import FastAPI
from config.database import SessionLocal, engine, init_db, Base
from models import wishlist_values, wishlist
from routes import wishlist_routes, wishlist_values_routes, ticker_details_routes
init_db()
app = FastAPI()

app.include_router(wishlist_routes.router)
app.include_router(wishlist_values_routes.router)
app.include_router(ticker_details_routes.router)

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to SmartInvestor"}

@app.get('/test')
def test():
    return {"message": "Welcome to SmartInvestor"}





Base.metadata.create_all(bind=engine)