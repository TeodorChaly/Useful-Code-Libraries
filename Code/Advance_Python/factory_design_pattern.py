from abc import ABCMeta, abstractmethod


# Dynamically decide which class to instantiate

class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        """" Interface method """


class Student(IPerson):
    def __init__(self):
        self.name = "Student "

    def get_name(self):
        print("I am a student")


class Teacher(IPerson):
    def __init__(self):
        self.name = "Teacher "

    def get_name(self):
        print("I am a teacher")


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        elif person_type == "Teacher":
            return Teacher()
        else:
            print("Invalid person type")
            return None


choice = input("What kind of person do you want to create? ")
person = PersonFactory.build_person(choice)
person.get_name()
