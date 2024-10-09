from .base import Base

class Band(Base, table=True):
    __tablename__ = "bands"

    band_genre: str
    band_name: str
    band_album: str
    band_members: str