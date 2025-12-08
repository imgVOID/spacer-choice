from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    is_admin: bool
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    """Successful login answer"""
    access_token: str
    token_type: str = "bearer"
