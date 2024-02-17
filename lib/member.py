from lib.db.db import BASE
from sqlalchemy import Column, Integer, String, DateTime, Float

"""
This is a sub class for members who are  registered
"""

class Member(BASE):

    __tablename__ = "members"

    id = Column(Integer(), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    balance = Column(Float, default=0.0)



if __name__ == "__main__":
    import ipdb

    ipdb.set_trace()