from .base import Base
from sqlmodel import Field

class Member(Base, table=True):
    __tablename__ = "members"

    name: str
    role: str
    join_date: int
    leave_date: int = None
    band_id: int = Field(default=None, foreign_key="bands.id")
