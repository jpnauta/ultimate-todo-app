from sqlalchemy import Column, Integer, String

from modules.core.db import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(String)
