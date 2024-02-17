from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///lib/db/sportif.db")
BASE = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
