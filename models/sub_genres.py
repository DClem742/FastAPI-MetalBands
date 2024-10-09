from .base import Base
from sqlmodel import Field

class Sub_Genre(Base, table=True):
    __tablename__ = "sub_genres"

    type: str
    band_id: int = Field(default=None, foreign_key="bands.id")