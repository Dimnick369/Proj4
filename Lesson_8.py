# region  stars

# numbers = [2, 1, 3, 4, 7]
# more_numbers = [*numbers, 11, 18]
# # # print(more_numbers[0], sep=',ZZ ')
# # print(more_numbers, sep=' ZZ ')
# print(*numbers, sep=' ZZ ')
# print(numbers[0],numbers[1],numbers[2], sep=' ZZ ')

########################################
# #
# fruits = ['lemon', 'pear', 'watermelon', 'tomato']
# numbers = [2, 1, 3, 4, 7]
# print(*numbers, *fruits ,sep=' Z ')

########################################
# #
# fruits = ['lemon', 'pear', 'watermelon', 'tomato']
#
# first, second, *remaining = fruits
# print(first, second, remaining)
# first, *middle, last = fruits
# print(first, middle, last)

########################################

# date_info = {'year': "2020", 'month': "01", 'day': "01"}
# filename = "{year}-{month}-{day}.txt".format(**date_info)
# print(filename)
# print(date_info.items())
# print(*date_info.items())
# ########################################
#
# fruits = ['lemon', 'pear', 'watermelon', 'tomato']
# first, second, *remaining = fruits
#
# first_word, *other_fruits = fruits
# print(first_word,other_fruits)
# #
# first_letter, *remaining=first_word
# print(first_letter,remaining)
#
# (first_letter, *remaining), *other_fruits = fruits
# print(first_letter,remaining,other_fruits)
#
# (first_letter, *remaining, last_letter ), *other_fruits = fruits
# print(first_letter,remaining,last_letter,other_fruits)
# #
# (first_letter, *remaining),(), *other_fruits = fruits
# print(first_letter,remaining,first_letter2,remaining2,other_fruits)

########################################

# def palindromify(sequence):
#     return list(sequence) + list(reversed(sequence))
#
# def palindromify1(sequence):
#     return [*sequence, *reversed(sequence)]
#
# print(palindromify([1,2,3,4,5]))
# print(palindromify1([1,2,3,4,5]))

########################################

# def rotate_first_item(sequence):
#     return [*sequence[1:], sequence[0]]


# endregion
##################################################
# region func
#
# def min2(a,b):
#     if a<b:
#         return a
#     else:
#         return b
# #
# # res=min2(5,10)
# # print(res)
# # print(min2(12,8))
# print(min2(min2(3,2),1))

################################ Без возврата

# def mess(a):
#     print(f'Hello efger {a}')
#     # return
#
# mess('Dima')

################################ Произвольное число параметров

# def min2(*a):
#     m=a[0]
#     print(a)
#     for i in a:
#         if i <m:
#             m=i
#     return m
#
# # print(min2(12,8))
# print(min2(*[12,3,7,4,2,7,9,1])) #!!!!!!!!!!!!!

################################ Cо значением по умочанию

# def steps(st,end=10,step=1):
#     for i in range(st,end,step):
#         print(i,end=' ')
# #
# steps(6)
# print('ZZZZZZZZ')
# steps(2,5)
# print('ZZZZZZZZ')
# steps(2,8,2)
#
# steps(2,8,2,6)

################################ Именованные переменные

# def steps(st,end=10,step=1):
#     for i in range(st,end,step):
#         print(i,end=' ')
#
# steps(end = 20, st= 5)
# print('ZZZZZZZZ')

# endregion
##################################################
# region Local Global
################################ Локальность
# d=100
#
# def init_values():
#     print(d)
#
# init_values()



# def init_values(a):
#     a=100
#     print(id(a))
#
# a=10
# print(id(a))
# init_values(a)
# print(a)


# def init_values(b):
#     b.append(100)
#     print(id(b))
#
# a=[10,20]
# print(id(a))
# init_values(a)
# print(a)


# def init_values(b):
#     b.append(100)
#     b=[200,300,400]
#     b.append(678500)
#
# a=[10,20]
# init_values(a)
# print(a)

################################ Глобальность

# def printc():
#     print(a)
#
# a=15
# printc()


# def printc():
#     print(a)
#     a=10
#     print(a)
#
# a=15
# printc()
# print(a)

# endregion
##################################################
# region func2+Global/Local
# def first():
#     pass
# print(dir())
# a=[1,2,3,4,5]
# print(dir())
# ########################### Local
# t=18
# tmp='OK'
#
# def f(t):
#     t=t+23
#     tmp='NO'
#     print(t,tmp)
#     return t,tmp,1,2,3,4,5,7,8
#
# a=f(t)
# print(*a,sep=' ZZ ')
# print(t,tmp)
# ########################### NS + Область видимости
# def b():
#     print(2,dir())
#     x=31
#     print(3,dir())
#     def a():
#         print(6,dir())
#         print(x)
#         print(7,dir())
#
#     print(4,dir())
#     a()
#     print(5,dir())
#
# print(1,dir())
# b()
# print(8,dir())
########################### NS2+ Область видимости


# def b():
#     print(2,dir())
#     x=31
#     a()
#     print(5,dir())
#
# def a():
#     print(3, dir())
#     print(x)
#     print(4, dir())
#
# print(1,dir())
# b()
# print(6,dir())


########################### global + nonlocal mode
# x=64
# def b():
#     x=31
#     def a():
#         print(x)
#     a()
# b()
# ############################# global
# x=64
# def b():
#     x=31
#     def a():
#         global x
#         print(x)
#     a()
# b()
############################# nonlocal
# x=64
# def b():
#     x=31
#     def a():
#         nonlocal x
#         x=21
#         print(x)
#     a()
#     print(x)
#
# b()
# print(x)
############################# if+for

# a=30
# y=100
# if a>5:
#     y=0
#     print(y)
# print(y)

# ##############################
# for i in [1,2,3,4]:
#     print(i)
# print(i)
# ##############################
# for i in []:
#     y=0
# print(y)
########################### FacePalm
# print(dir())
#
# def a(c=[2]):
#     c.append(2)
#     print(c)
#
# print(dir())
# a()
# print(dir())
# a()
# print(dir())
# a()
# print(dir())
# a()
# endregion
##################################################
# region decor
#
# def f():
#     print('Usual func')
#
# def decor(infunc):
#
#     # infunc=body f
#
#     def decorated():
#         print('Begin')
#         infunc()
#         print('End')
#
#
#     return decorated
#
# f()
# print('###########')
# b=decor(f)
# b()
# print('###########')
# f=decor(f)
# f()

######################################################### deco sugar

# def decor1(infunc):
#     def decorated():
#         print('Begin1')
#         infunc()
#         print('End1')
#
#     return decorated
#
# def decor(infunc):
#     def decorated():
#         print('Begin')
#         infunc()
#         print('End')
#
#     return decorated
#
# @decor1
# @decor
# def f():
#     print('Usual func')
#
# f()

######################################################### attrs to deco

# def decor(infunc):
#
#     def decorated(a):
#         print('Begin')
#         if len(a)>6:
#             print('Add ' + a)
#         infunc('wertyujhgfd')
#         # infunc(a)
#         print('End')
#
#     return decorated
#
# @decor
# def f(a):
#     print('Usual func: ' + a)
#
# f('New block')
# print('ZZZZZZZZZZ')
# f('New')

######################################################### universal deco (with stars)
#
# def decor(infunc):
#     def decorated(*a):
#         print('Begin')
#         if len(a)>0:
#             print('Add ' + a[0])
#         infunc(*a)
#         print('End')
#
#     return decorated
#
# @decor
# def f():
#     print('Usual func: ')
#
# @decor
# def f1(a):
#     print('Usual func: '+a)
#
# f()
# print('ZZZZZZZZZZZZZZZZZ')
# f1('New Block')

# endregion
##################################################
# region  lmbda+sort
#
# a=[
#     [123,234,345],   #1
#     [1,2,3],         #0
#     [5,5,5,5,5,5,5], #7
#     [12345,12345,123456] #3
# ]
#
# a.sort(key=lambda x:' '.join( map(str,x)).count('5'))
# print(a)

# endregion