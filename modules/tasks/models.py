from sqlalchemy import Column, String

from modules.core.models import BaseModel


class Task(BaseModel):
    __tablename__ = 'tasks'
    name = Column(String)
    content = Column(String)
