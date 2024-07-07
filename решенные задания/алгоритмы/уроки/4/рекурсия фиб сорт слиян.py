import random

# факториал
# n = 10
# fact = 1
# for i in range(1, n + 1):
#     fact =fact * i

# def fact_r(n):
#     if n <= 1:
#         return 1
#     return n * fact_r(n - 1)

# n = 100
# fact = fact_r(n)
    
# print(f'Факториал {n} равен {fact}')

# фибоначи 
# fib1 = fib2 = 1
# # print(fib1, fib2, end=' ')
# n = 20
# for i in range(2, n):
#     summa = fib2 + fib1
#     fib1 = fib2
#     fib2 = summa
#     # print(summa, end=' ')
# print(fib2)

# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print (fib(20))

#слияние сортировка
def merge(arrl, arrr):
    sorted_arr = list()
    curent_left = 0
    curent_right = 0
    
    lenl = len(arrl)
    lenr = len(arrr)
    
    for i in range(lenl + lenr):
        if curent_left < lenl and curent_right <lenr:
            if arrl[curent_left] > arrr[curent_right]: # > от большего к меньшему, < от меньшего к большему
                sorted_arr.append(arrl[curent_left])
                curent_left += 1
            else:
                sorted_arr.append(arrr[curent_right])
                curent_right += 1
        else:
            if curent_left == lenl:
                for j in range(curent_right, lenr):
                    sorted_arr.append(arrr[j])
            else:
                for j in range(curent_left, lenl):
                    sorted_arr.append(arrl[j])
            break
    return sorted_arr
    

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_side = arr[:mid]
    right_side = arr[mid:]
    
    # for i in range(0, mid):
    #     val = arr[i]
    #     left_side.append(val)
    
    # for i in range(mid, len(arr)):
    #     val = arr[i]
    #     right_side.append(val)
    
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)
    
    result = merge(left_side, right_side)
    return result

n = 50
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)
    
print (arr)
print (merge_sort(arr))