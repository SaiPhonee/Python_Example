# 27. Определить количество цифр в числе
n = 12345
i=0
while n > 0:
    n=n//10
    i+=1
print(i)