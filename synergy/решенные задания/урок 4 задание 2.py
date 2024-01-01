print('Введите целое пятизначное число (через пробел, например: 1 2 3 4 5):')
a,b,c,d,e= map(int,input().split())
x= float((d**e*c)/(a-b))
print(x)