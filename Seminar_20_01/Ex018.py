# 18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
print ('x y  F')
for x in range (2):
    for y in range (2):
        print(x, y, (not (x or y)) == (not x) and (not y))