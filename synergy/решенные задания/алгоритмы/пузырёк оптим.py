from random import randint

def sort(list):
    srav = 0 #считаем кол-во сравнений
    tmp = True
    tmpn = 0 #переменная для уменьшения длинны цикла, так как в каждый цикл мы передвигаем число в крайнее положение
    while(tmp):
        tmp = False
        for i in range(len(list) - tmpn - 1):
            srav += 1
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                tmp = True
        tmpn += 1
    if tmpn == 1:
        print("список не требует сортирвки ")
    print("кол-во сравнений: ", srav)
    return list

N = 20
list = [] #генерируем список с N элементами от 1 до 99
for i in range(N):
    list.append(randint(1, 99))

print("не сортированный список: ", list)
print("список после сортировки: ", sort(list))