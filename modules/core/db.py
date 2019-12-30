from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from modules.core.settings import DATABASE_URL

engine = create_engine(DATABASE_URL, convert_unicode=True)
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)
