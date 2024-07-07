n=int(input('Введите количество элементов списка '))
sp1 = list(map(int, input('Введите элементы списка через пробел: ').split()))[:n]
e=set(sp1)
print(len(e))