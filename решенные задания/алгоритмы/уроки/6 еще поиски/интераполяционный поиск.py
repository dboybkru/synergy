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
arr.sort() #интераполяционный поиск

left = 0
right = n - 1
while left < right and to_search >= arr[left] and to_search <= arr[right]:
    part1 = float(right - left) / (arr[right] - arr[left])
    part2 = to_search - arr[left]
    ind = left + int(part1 * part2)
    
    if arr[ind] == to_search:
        answer = ind
        break
    if arr[ind] <to_search:
        left = ind + 1
    else:
        right = ind + 1
###############################################

print(arr)
if answer != -1:
    print(f'Элемент в списке был, его индекс: {answer}')
else:
    print('Элемент в списке отсутствует')