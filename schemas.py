from pydantic import BaseModel

# Schema for User Sign-Up
class UserCreate(BaseModel):
    prn: str
    name: str
    email: str
    password: str

# Schema for User Login
class UserLogin(BaseModel):
    prn: str
    password: str

