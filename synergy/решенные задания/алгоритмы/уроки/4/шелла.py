from random import randint

def sort(list, N):
    step = len(list) // 2
    while step > 0:
        for i in range(step,N, 1):
            curent_index = i
            index_to_check = curent_index - step
            while curent_index > 0 and list[index_to_check] > list[curent_index]:
                temp = list[curent_index]
                list[curent_index] = list[index_to_check]
                list[index_to_check] = temp
                curent_index -= step
                index_to_check -= step
        step = step // 2
    return list

N = 20

list = [] #генерируем список с N элементами от 1 до 99
for i in range(N):
    list.append(randint(1, 99))


print("не сортированный список: ", list)
print("список после сортировки: ", sort(list, N))


# def sort(list, N):
#     step = len(list) // 2
#     while step > 0:
#         for i in range(step,N, 1):
#             value = list[i]
#             curent_index = i
#             index_to_check = curent_index - step
#             while curent_index > 0 and list[index_to_check] > value:
#                 list[curent_index] = list[index_to_check]
#                 curent_index -= step
#                 index_to_check -= step
#             list[curent_index] = value
#         step = step // 2
#     return list