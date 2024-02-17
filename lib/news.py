from lib.db.db import BASE
from sqlalchemy import Column, Integer, String, DateTime, Float

"""
This is a sub class for News content inventory. 

This should be a read only database
"""

class News(BASE):

    __tablename__ = "news"

    id = Column(Integer(), primary_key=True)
    title = Column(String())

    



if __name__ == "__main__":
    import ipdb

    ipdb.set_trace()