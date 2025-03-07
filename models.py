from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, TIMESTAMP, text
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    prn = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String, nullable=False)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_prn = Column(String(20), ForeignKey("users.prn", ondelete="CASCADE"))
    food_item = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=False)
    order_status = Column(String(50), default="Pending")
    order_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

