def get_name(name):
    if not isinstance(name,str):
        return TypeError
    return name.capitalize()



class Wallet:
    def __init__(self, balance=0):
        self.balance = balance

    def spend_cash(self, amount):
        self.amount = amount
        if self.balance >= self.amount:
            return self.balance - self.amount
        # return 'InsufficientAmount'
        raise Exception('InsufficientAmount') #olmalidi
    
    def add_cash(self, amount):
        self.amount = amount
        return self.balance + self.amount
        
        

