a=set(map(int,input('Введите элементы 1го списка через пробел: ').split()))
b=set(map(int,input('Введите элементы 2го списка через пробел: ').split()))
print (f'В списках {len(a.intersection(b))} одинаковых чисел')