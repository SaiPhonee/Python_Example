# 2. Даны два числа. Показать большее и меньшее число
number1 = int(input("Введите 1 число "))
number2 = int(input("Введите 2 число "))
if number1 > number2:
    print(f'Большее число {number1}, меньшее {number2}')
elif number1 == number2:
    print('Числа равны')
else:
    print(f'Большее число {number2}, меньшее {number1}')
