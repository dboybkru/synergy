def tmp(x):
    print(my_list[x])
    x += 1  
    if x == n:
        print('Конец списка. ')
        return
    tmp(x)

x = 0
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = int(len(my_list))
tmp(x)