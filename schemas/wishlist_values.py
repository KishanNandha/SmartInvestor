from pydantic import BaseModel


class WishlistValueBase(BaseModel):
    wishlist_id: int
    string_value: str


class WishlistValueCreate(WishlistValueBase):
    pass


class WishlistValueOut(WishlistValueBase):
    value_id: int

    class Config:
        orm_mode = True
