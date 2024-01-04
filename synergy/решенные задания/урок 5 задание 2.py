word = (input("Введите слово: ")) 
a = word.count('a') 
e = word.count('e') 
i = word.count('i') 
o = word.count('o') 
u = word.count('u') 
y = word.count('y') 
x= len(word)
x1=0
x2=0
if a == 0: 
    print("a = False")
else: 
    x1+=a
if e == 0: 
    print("e = False")
else: 
    x1+=e 
if i == 0: 
    print("i = False") 
else: 
    x1+=i
if o == 0: 
    print("o = False") 
else: 
    x1+=o
if u == 0: 
    print("u = False") 
else: 
    x1+=u
if y == 0:  
    print("y = False") 
else: 
    x1+=y
x2=x-x1
print("Гласных: ",x1) 
print("Согласных: ", x2)