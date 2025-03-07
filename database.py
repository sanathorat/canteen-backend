from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL Database URL (Replace 'your_password' with your actual PostgreSQL password)
DATABASE_URL = "postgresql://canteen_admin:louistomlinson@localhost/canteen_ordering"

# Create Engine
engine = create_engine(DATABASE_URL)

# Create Session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base Class for Models
Base = declarative_base()

