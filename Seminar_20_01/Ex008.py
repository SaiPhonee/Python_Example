# 8. Показать четные числа от 1 до N
n = int(input('Введите число '))
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
