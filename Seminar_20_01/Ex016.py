# 16. Дано число обозначающее день недели. Выяснить является номер дня недели выходным 
n = int(input('Введите число '))
if 6<=n<=7:
    print('Выходной')
elif 1<=n<=5:
    print('Будни')
else:
    print('Не верно введено число')