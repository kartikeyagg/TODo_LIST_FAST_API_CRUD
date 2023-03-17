from sqlalchemy import Column, Integer, String

from config.db import BASE

class TODO(BASE):

    __tablename__ = "todotable"

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(31))
    description = Column(String(254)  )



