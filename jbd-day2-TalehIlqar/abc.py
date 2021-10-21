from abc import ABC, abstractmethod


# class Animal(ABC):
#     def __init__(self, name, color):
#         self.name = name  
#         self.color = color 

#     @abstractmethod
#     def movee(self):
#         return 'salam1'

# class Cat(Animal):
#     def movee(self, like):
#         # self.name=name
#         self.like=like
#         # return 'salam'
#         return f'{self.like}'
        

# anm1 = Cat("name", 'color')
# print(anm1.movee('sag ol'))


class Animal(ABC):
    def __init__(self, name):
        self.name=name
        
    def tiger(self, name, foot):
        self.name = name
        self.foot = foot
        return f'{self.name}, {self.foot}'
      

    @abstractmethod  
    def Domestic_animals(self, color):
        self.color=color
        print(f'{self.name},{self.color}') #name-i name kimi print edir amma men toplan yazdigimda bu selfle bagli amma niye?


class WhildAnimal(Animal):
    def __init__(self, foot, voice):
        self.foot = foot
        self.voice = voice
        
        
    def Domestic_animals(self,name, color):
        self.color=color
        self.name=name
        return f'{self.name},{self.color}'
      
    
    def tiger(self, name, foot):
        self.name = name
        self.foot = foot
   
        print(f'{self.name},{self.foot}')
        
x = Animal
a = x.Domestic_animals('red','name')
print(a)

# abstractmethod ne uchundur?