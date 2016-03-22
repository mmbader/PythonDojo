__author__ = 'cabarca'
class Person(object):

    def __init__(self):
        self.__firstName = None

    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, name):
        self.__firstName = name.title()

person1 = Person()
person1.firstName = 'john'

print (person1.firstName)
