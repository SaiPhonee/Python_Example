# 20. Задать номер четверти, показать диапазоны для возможных координат
a = int(input('Введите номер четверти '))
if a == 1:
    print('x>0 and y>0')
if a == 2:
    print('x<0 and y>0')
if a == 3:
    print('x<0 and y<0')
if a == 4:
    print('x>0 and y<0')
