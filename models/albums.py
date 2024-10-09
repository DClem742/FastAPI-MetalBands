from .base import Base

class Album(Base, table=True):
    __tablename__ = "albums"

    album_name: str
    release_date: int