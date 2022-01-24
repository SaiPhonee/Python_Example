# 23. Показать таблицу квадратов чисел от 1 до N 
n = 5
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i*j, end = ' ')
    print()