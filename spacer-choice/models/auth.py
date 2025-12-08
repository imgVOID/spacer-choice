from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base # Импортируем наш базовый класс


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String) 
    is_admin = Column(Boolean, default=False)

    objects = relationship("CelestialObject", back_populates="creator")
