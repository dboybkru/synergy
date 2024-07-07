import random
x = (int(input('Введите размер матрицы по Х:')))
y = (int(input('Введите размер матрицы по Y:')))
sp1 = [[(random.randint (-100, 100)) for i in range(x)] for j in range(y)]
sp2 = [[(random.randint (-100, 100)) for i in range(x)] for j in range(y)]
result = [[sp1[i][j] + sp2[i][j] for j in range(x)] for i in range(y)]
print (*sp1)
print (*sp2)
print (result)