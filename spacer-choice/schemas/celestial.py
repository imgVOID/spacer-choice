from pydantic import BaseModel, Field


class CelestialObjectBase(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    right_ascension: float = Field(ge=0.0, le=360.0) 
    declination: float = Field(ge=-90.0, le=90.0)     
    description: str | None = None


class CelestialObjectCreate(CelestialObjectBase):
    """Create celestial POST response body"""
    pass


class CelestialObjectRead(CelestialObjectBase):
    """Read celestial GET response body"""
    id: int
    creator_id: int
    
    class Config:
        from_attributes = True 
