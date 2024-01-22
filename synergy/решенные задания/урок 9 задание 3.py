sp=list(map(int,input('Введите элементы списка через пробел: ').split()))
a=set()
for i in sp:
    if i not in a:
        a.add(i)
        print(f'{i} NO')
    else:
        print(f'{i} YES')