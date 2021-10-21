import unittest
from unittest.case import TestCase


def kub_funk(number):
    if not isinstance(number, int):
        raise TypeError
    return number ** 3

# print(kub_funk('string'))

nameList = ['alma', 3, True, 'proqramçı']
def Task_2(letter):
    if isinstance(letter, int):
        raise TypeError
    else:
        nameList2 = []
        for word in nameList:
            if letter in str(word):
                nameList2.append(word)
        return nameList2

# print(Task_2('o'))

class Person:
    def __init__(self, name, surname):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        
    def get_fullname(self):
        return f'{self.name} {self.surname}'

# x = Person("Koroglu", "Mirzeyev")
# print(x.get_fullname())

