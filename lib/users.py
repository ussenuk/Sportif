class User:

    def __init__(self, name, email, city, country):
        self._name = name
        self.email = email
        self.city = city
        self.country = country


    def get_name(self):
        return self._name
    
    name = property(get_name)

if __name__ == "__main__":
    pass