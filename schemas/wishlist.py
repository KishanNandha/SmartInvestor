from pydantic import BaseModel


class WishlistBase(BaseModel):
    name: str


class WishlistCreate(WishlistBase):
    pass


class WishlistOut(WishlistBase):
    wishlist_id: int

    class Config:
        orm_mode = True

