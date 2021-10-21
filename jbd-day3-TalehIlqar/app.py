# # *** task1 ***

# n = 0
# def whl(num):
#     while True:
#         global n
#         n += num
#         yield n


# run_2 = whl(13)
# print(next(run_2))
# print(next(run_2))
# print(next(run_2))
# print(next(run_2))


# *** task 2 ***
# l = [0,2,3,4,5,7]

# def ink(n):
#     return n**2
# new_lis = list(map(ink, l))
# print(new_lis)

# # diger listi quvvete yukseltme
# squares=list(map(lambda t : pow(t,2),l))
# print(squares)

# *** task 3 ***
# lis = [0,2,3,4,5,7, 15, 45]
# def ink(num):
#     if num % 3 or num % 5:
#         return False
#     return True
    
# new_lis = list(filter(ink, lis))
# print(new_lis)

# *** task 4 ***
# ad=['Babək', 'Ali', 'Koroğlu']
# soyaq=['Veliyev', 'Ahmedov', 'Recebov']
# yaş=[23, 54, 98]


# x = zip(ad, soyaq, yaş)
# print(list(x))
# print(tuple(x))

# *** task 5 ***


# from functools import reduce

# my_list = [3, 5, 6]
# def get_num(x, y):
#     return x + y


# item = reduce(get_num, my_list)
# print(item)



# l = [3,20, 15, 30, 45, 90,100]
# def b(n):
#     return n
# s = list(map(filter(n % 3 or n % 5)))
# print(s)

# ***************
# num = 0
# def infinite_sequence(num):
    
#     while True:
#         yield num 
#         num += num
# x = infinite_sequence(13)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))