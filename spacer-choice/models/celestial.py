from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base


class CelestialObject(Base):
    __tablename__ = "celestial_objects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    right_ascension = Column(Float) 
    declination = Column(Float)     
    description = Column(String, nullable=True)

    creator_id = Column(Integer, ForeignKey("users.id")) 
    creator = relationship("User", back_populates="objects")
