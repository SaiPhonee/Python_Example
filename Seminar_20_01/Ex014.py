# 14. Найти третью цифру числа или сообщить, что её нет
a = int(input('Введите число '))
if a // 100 > 0:
    print(a//100%10)
else:
    print('Третьей цифры нет')