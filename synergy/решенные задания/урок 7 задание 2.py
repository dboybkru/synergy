n = int(input('Введите количество элементов: '))
print('Введите числа для добавления в список через пробел (ввести можно много чисел, однако в список будет добавлено не более ', n, ' элементов):')
a = list(map(int, input().split()))[:n] #В список будут добавлены элементы по индекс n
b = []
nn = int(n/2)
for i in range(nn):
    x = i+1
    b.append(a[-x])
    b.append(a[i])
if n <= 10:
    if int((n/2)%2) == 0:    
        b.append(a[nn])
elif int((n/2)%2) != 0:    
    b.append(a[nn])
print(b)