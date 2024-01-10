n = int(input('Введите кол-во целых чисел:'))
x = 0
for i in range(n):
    a = int(input('Введите целое число:'))
    if a == 0:
        x += 1
print ('0 было введено:', x, 'раз')