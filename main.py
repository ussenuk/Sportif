import ipdb

from lib.db.db import BASE, engine, session

from lib import Non_Member, Member, News



if __name__ == "__main__":
    print("Register Yourself to Sportif as member")

    
    BASE.metadata.create_all(engine)

    # densel = Non_Member(name="Densel",
    #                 email="user@gmail.com",
    #                 city="Nairobi", 
    #                 country="Kenya", 
    #                 gender="Male", 
    #                 age="27")
    
    # session.add(densel)
    # session.commit()

 

    ipdb.set_trace()