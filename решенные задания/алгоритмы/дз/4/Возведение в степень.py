import sys
sys.setrecursionlimit(1000000) 
def degree(x, y):
    if (x < y):
        return degree(y, x)
    elif (y != 0):
        return (x + degree(x, y-1))
    else:
        return 0
print(degree(15, 250))