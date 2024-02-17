from users import User

class Member(User):
    def __init__(self, gender, age):
        super().__init__(name, email, city, country)
        self.gender = gender
        self.age = age

if __name__ == "__main__":
    import ipdb

    ipdb.set_trace()