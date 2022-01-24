# 21. Программа проверяет пятизначное число на палиндромом.
number = 12321
n1 = number // 10000
n2 = number / 1000 % 10
n4 = number // 100 % 10
n5 = number % 10
if n1==n5 and n2==n4:
    print('Является')
else:
    print('Не является')