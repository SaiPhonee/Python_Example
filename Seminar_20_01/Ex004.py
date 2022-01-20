# 4. Найти максимальное из трех чисел
number1 = int(input("Введите 1 число "))
number2 = int(input("Введите 2 число "))
number3 = int(input("Введите 3 число "))
max = number1
if number2 > max:
    max = number2
if number3 > max:
    max = number3
print(f'Максимальное число {max}')
