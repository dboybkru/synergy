print('Введите целое число:')
a=int(input())
b= a % 2
if (a < 0):
    if b == 0:
        print('отрицательное четное число')
    else:
        print('отрицательное нечетное число')
else:
    if a ==0:
        print('Число равно 0')
    else:
        if b == 0:
            print('положительное четное число')
        else:
            print('положительное нечетное число')
    