# from abc import ABC, abstractmethod


# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name

#     def prin(self):
#         print(self.name)    
    
#     def move(self):
#         pass

# class Cat(Animal):
#     def __init__(self, color, name):
#         self.color = color
#         super().__init__(name)

#     def prinColor(self):
#         print(self.color)
       

#     # def move(self):
#     #     return "run"
        


# anm1 = Cat("red1",'red2')
# # print(Cat('toplan').move())
# anm1.prin()
# # Cat("red2").prin()

# class Person:
#     __age = 40
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
    
#     def introduce(self):
#         return f'my name is {self.__name} and surname is {self.__surname}'
    
#     def get_age(self):
#         return self.__age
    

#     def set_name(self, name):
#         if len(name) < 2:
#             raise Exception("charachter must be 2 and better")
#         else:
#             self.__name=str(name)
        
# x = Person('Taleh', 'Ilqar')
# # x.set_name("Vusal")

# print(x.introduce())

class lfd:
    def __init__(self, name) -> None:
        self.name = name
    
    def su(self):
        return f'my name is {self.name}'
    
x = lfd('Taleh')
print(x.__dict__)
    