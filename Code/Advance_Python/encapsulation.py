class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):  # Setter - control over class
        if value == "":
            self.__name = "No name"
        else:
            self.__name = value

    @staticmethod
    def static_method():
        print("I am static method")


p1 = Person("Mike", 20, 'm')
print(p1.Name)
p1.Name = ""
print(p1.Name)
Person.static_method()