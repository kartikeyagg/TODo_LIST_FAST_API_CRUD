
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url = "sqlite:///./todo.db"

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/test1")
# engine = create_engine(db_url, connect_args={"check_same_thread":False})

sessionlocal = sessionmaker(autocommit = False, bind = engine,autoflush=False)

BASE = declarative_base()

conn = engine.connect()

