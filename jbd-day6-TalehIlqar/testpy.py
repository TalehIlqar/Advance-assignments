from main import get_name, Wallet


def test_Task1():
    assert get_name('tech') == 'Tech'
    # assert get_name(22) == 22
    # AssertionError (TypeError, get_name, 33)    # niye str de yazanda ishleyir
    
def test_Task2_1():
    assert Wallet(123).spend_cash(0) == 123
    AssertionError(TypeError, Wallet, 'sting') # niye int de yazanda ishleyir
    
def test_Task2_2():
    assert Wallet(120).spend_cash(30) == 90
    
def test_Task2_3():
    assert Wallet(10).add_cash(70) == 80
    
# def test_Task2_4():
#     assert Wallet(60).spend_cash(90) == -30
