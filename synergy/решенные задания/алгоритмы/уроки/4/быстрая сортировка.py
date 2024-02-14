import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    ind_off_str_el = random.randint(0, len(arr) - 1)
    str_el = arr[ind_off_str_el]
    low = list()
    mid = list()
    high = list()
    
    for el in arr:
        if el == str_el:
            mid.append(el)
        elif el < str_el:
            low.append(el)
        else:
            high.append(el)
    
    low = quick_sort(low)
    high = quick_sort(high)
    result = low + mid + high
    return result
    
n = 50
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)
    
print (arr)
print (quick_sort(arr))