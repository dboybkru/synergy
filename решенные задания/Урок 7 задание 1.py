n = int(input('Введите количество элементов: '))
a = 0
b = []
for i in range(n):
    a = int(input('Введите число: '))
    b.append(a)
b.reverse()
print(b)