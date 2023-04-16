import datetime

class People:
    current_year = datetime.datetime.today().year

    def __init__(self, name, age, function, hiring_year):
        self.name = name
        self.age = age
        self.function = function
        self.employed_time = self.employed_time(hiring_year)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, str):
            value = int(value)
        self._age = value

    @classmethod
    def employed_time(cls, hiring_year):
        employed_time = cls.current_year - hiring_year
        return employed_time


employee1 = People('Mark', '45', 'Manager', 2009)
employee2 = People('John', 23, "Seller", 2020)

print(employee1.__dict__)
print(employee2.__dict__)