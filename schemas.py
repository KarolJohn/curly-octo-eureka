from pydantic import BaseModel
# --- Pydantic User Schemas ---
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    text: str
class ItemCreate(ItemBase):
    pass
class Item(ItemBase):
    id: int
    class Config:
        orm_mode = True

class TokenData(BaseModel):
    username: str | None = None