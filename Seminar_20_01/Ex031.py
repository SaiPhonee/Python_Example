# Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.
def create_list(n):
    list=[]
    res=1
    for i in range (0, n+1):
        if i%2==0:
            res=3**i
            list.append(res)
        else:
            res=-3**i
            list.append(res)
    return list

print(create_list(5))
