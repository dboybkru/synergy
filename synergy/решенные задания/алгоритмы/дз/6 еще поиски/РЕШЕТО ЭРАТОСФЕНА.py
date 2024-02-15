n = 20
arr = []
for i in range(n):
    arr.append(i)
    
arr[1] = 0

###############################################
for i in range(n):
    if arr[i] != 0:
        j = i * 2
        while j < n:
            arr[j] = 0
            j += i
###############################################

for i in arr:
    if i !=0:
        print(i, end=' ')