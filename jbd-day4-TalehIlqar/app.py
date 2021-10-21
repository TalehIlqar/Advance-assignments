import json

class Car:
    def __init__(self, name, engine, price):
            self.name = name
            self.engine = engine
            self.price = price

    def myfunc(self):
        return f'{self.name}, {self.engine},{self.price}'

p1 = Car("M5", "3.5L", 32000)

jsonStr = json.dumps(p1.__dict__)

with open('car_1.json', 'w') as m:
    m.write(jsonStr)

#Dumps to Dict
# ************* task2


p2 = Car("Elantra", "2.2L", 17000)

jsonStr2 = json.dumps(p2.__dict__)

with open('car_2.json', 'w') as m:
    m.write(jsonStr2)
   

with open('car_2.json', 'r') as n:
    carObj2 = json.load(n)
    print(carObj2['name'])
    print(carObj2['engine'])
    print(carObj2['price'])

#Dict to load
# ************* task3
with open('car_3.json', 'r') as n:
    carObj3 = json.load(n)

l = []
for i in carObj3:
    l.append(i['name'])

print(l)

