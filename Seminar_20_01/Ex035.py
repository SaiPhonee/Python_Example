# Написать программу получающую набор произведений чисел от 1 до N.
def mylt(n):
    res = 1
    list= []
    for i in range(1, n+1):
        res*=i
        list.append(res)
    return list
print(mylt(6))