# Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму
def sum_list(n):
    list=[(1+(1/i)**i) for i in range (1, n+1)]
    return sum(list)

print(sum_list(5))