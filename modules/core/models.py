import uuid

from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

from modules.core.db import db_session

Base = declarative_base()
Base.query = db_session.query_property()


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
