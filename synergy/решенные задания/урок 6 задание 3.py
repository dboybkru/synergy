a=int(input('Введите первое число: '))
b=int(input('Введите последнее число: '))
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=' ')