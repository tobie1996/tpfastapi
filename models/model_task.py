
from database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True)
    completed = Column(Boolean, default=False)
