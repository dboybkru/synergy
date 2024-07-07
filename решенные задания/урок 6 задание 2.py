x = int(input('Введите натуральное число: '))
a = 0
if x<0:
    print ('Введено отрицательное число')
    quit()
for i in range(1, x + 1):
    if x % i == 0:
        a += 1
print(a)