m = int(input('Введите максимальный вес лодки: '))
n = int(input('Введите количество рыбаков: '))
a = []
b = [] 
for i in range(n):
    a.append(int(input('Введите вес рыбака: ')))
for i in range(len(a)):
    if a[i] + min(a) <= m:
        b += [[a[i], min(a)]]
        a[i] += m
        a[a.index(min(a))] += m
    else:
        if a[i] > m:
            continue
        else:
            b += [[a[i]]]
print(b)
print(len(b))