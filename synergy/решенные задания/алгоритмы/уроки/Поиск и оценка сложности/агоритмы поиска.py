import random

n = 50
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)
    
to_search = random.randint(1,100)
print(to_search)
answer = -1

###############################################
# for i in range(n):  #линейный поиск
#     if arr[i] == to_search:
#         answer = i
#         break
###############################################

###############################################
arr.sort() #бинарный поиск

first = 0
last = n - 1
while first < last and answer == -1:
    mid_ind = (first + last) // 2
    if arr[mid_ind] == to_search:
        answer = mid_ind
    else:
        if arr[mid_ind] > to_search:
            last = mid_ind - 1
        else:
            first = mid_ind + 1
###############################################

print(arr)
if answer != -1:
    print(f'Элемент в списке был, его индекс: {answer}')
else:
    print('Элемент в списке отсутствует')