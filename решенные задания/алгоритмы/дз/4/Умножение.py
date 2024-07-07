import sys

def mult(a,b):
    if a==1:
        return b
    else:
        return b+mult(a-1,b)

sys.setrecursionlimit(1000000) 
print(mult(600,2800))