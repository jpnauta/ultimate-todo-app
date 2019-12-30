from sqlalchemy import Column, String

from modules.core.models import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    first_name = Column(String)
    last_name = Column(String)
