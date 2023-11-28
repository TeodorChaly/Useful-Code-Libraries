from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):
    @staticmethod
    def person_method():
        """ Interface method """


class Person(IPerson):
    def person_method(self):
        print("I am a person")


class ProxyPerson(IPerson):
    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("Proxy person")
        self.person.person_method()


p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()