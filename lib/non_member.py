from lib.db.db import BASE
from sqlalchemy import Column, Integer, String, DateTime


# from lib.users import User

# from users import User

"""
This is a sub class for non members who are supposed to register themselves
"""

class Non_Member(BASE):

    __tablename__ = "non_members"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    gender = Column(String())
    email = Column(String())
    city = Column(String())
    country = Column(String())
    age = Column(Integer())


    # def __init__(self, name, email, city, country, gender, age):
    #     super().__init__(name, email, city, country)
        
    #     self.gender = gender
    #     self.age = age

    #     self.register_member()

    # def register_member(self):
        # registration_form = ["Enter your name","Enter your gender","Enter your age", "Enter your email", "Enter your City", "Enter your Country"]
        # print("Please register yourself to Sportif")
        # for form in registration_form:
        #     print(form, ":")
        #     member[form]=input()
        # Member.members.append(self)

    # @classmethod
    # def get_all(cls):
    #     return [ {"name":mb.name, "gender":mb.gender, "country":mb.country} for mb in Member.members]

        

if __name__ == "__main__":
    import ipdb

    ipdb.set_trace()