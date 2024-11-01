from datetime import datetime as dt, timedelta as td
from sqlalchemy import Integer, DateTime, func, Interval
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base

class Video(Base):
    __tablename__ = 'video'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] 
    path: Mapped[str] 
    size: Mapped[int] 
    link: Mapped[str] = mapped_column(nullable=True)
    