def fakt(x):
    b = 1
    for i in range(x + 1):
        if i == 0:
            continue
        b = b * i
    return b
x = int(input('Введите максимальное число списка: '))
n = []
for i in range(x,0,-1):
    n.append(fakt(i))
print (n)