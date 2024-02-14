from random import randint

def sort(list):
    srav = 0 #считаем кол-во сравнений
    for i in range(0, len(list)-1): 
        for j in range(len(list)-1):
            srav += 1 
            if(list[j]>list[j+1]): 
                temp = list[j] 
                list[j] = list[j+1] 
                list[j+1] = temp
    print("кол-во сравнений: ", srav)
    return list 

N = 20
list = [] #генерируем список с N элементами от 1 до 99
for i in range(N):
    list.append(randint(1, 99))

print("не сортированный список: ", list)
print("список после сортировки: ", sort(list))