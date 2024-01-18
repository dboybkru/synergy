s1 = input('Введите строку (учитывается только 1000 символов): ')
s1 = s1[0:1000]
s2 = str()
a = 0
for b in s1:    
    if b != ' ':
        s2 += b
    else:
        if s2 [len(s2)-1:len(s2)] == ' ':
            continue
        else:
            s2 += b      
            #a = 0
print(s2)