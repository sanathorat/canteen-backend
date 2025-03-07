from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas
from passlib.context import CryptContext


# Initialize FastAPI
app = FastAPI()

# Create Tables
Base.metadata.create_all(bind=engine)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Canteen Backend is Running!"}

# ✅ API to Register New User (Sign-Up)
@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if PRN or email already exists
    existing_user = db.query(models.User).filter(
        (models.User.prn == user.prn) | (models.User.email == user.email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="PRN or Email already exists")

    # Hash the password before storing
    hashed_password = pwd_context.hash(user.password)
    new_user = models.User(prn=user.prn, name=user.name, email=user.email, password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

# ✅ API to Login User
@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    # Find user by PRN
    db_user = db.query(models.User).filter(models.User.prn == user.prn).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid PRN or Password")

    # Verify password
    if not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid PRN or Password")

    return {"message": "Login successful", "user": {"prn": db_user.prn, "name": db_user.name, "email": db_user.email}}
