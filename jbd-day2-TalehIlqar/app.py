class Number:
    def __init__(self, value):
        self.value = value


    # def __str__(self):


    def __add__(self, other):
        x = self.value + other.value 
        return x
    
    def __mul__(self, other ):
        y = self.value * other.value
        return y



    def __gt__(self, other):
        x = self.value
        y = other.value
        if x > y:
            return True
        else:
            return False

    def __lt__(self, other):
        x = self.value
        y = other.value
        if x < y:
            return True
        else:
            return False

    @staticmethod  # neye gore? yalniz selfi evez edir?
    def showValue(num):
        return num

number_1 = Number(16)
number_2 = Number(6)
number_3 = Number(5) # 3-cu elementi toplamaq olmur?
# print(number_1 + number_2 )
# print(number_1 * number_2 )
# print(number_1 > number_2)
# print(number_1 < number_2)
print(number_1.showValue(1))



