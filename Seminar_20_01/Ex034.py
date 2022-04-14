# Подсчитать сумму цифр в вещественном числе.
def sum_real_number(n):
    sum=0
    n=n.replace('-', '')
    n=n.replace('.', '')
    n=n.replace(',', '')
    n = int(n)
    while n>0:
        sum=sum+n%10
        n=n//10
    return sum
print(sum_real_number('-11'))