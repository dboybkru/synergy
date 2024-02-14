def bin(n):
    if n<2:
        print(n,end='')
    else:
        bin(n//2)
        print(n%2,end='')
 
 
bin(1300)