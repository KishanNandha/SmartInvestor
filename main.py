# app/main.py
from fastapi import FastAPI
from app.routes import wishlist_routes, wishlist_values_routes
from app.database import init_db

app = FastAPI()

app.include_router(wishlist_routes.router)
app.include_router(wishlist_values_routes.router)

if __name__ == "__main__":
    init_db()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
