from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from models import Base 
from conect_db import url

try:
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    print("Table for DB creates")

except SQLAlchemyError as e:
    print("Error creating tables:", e)