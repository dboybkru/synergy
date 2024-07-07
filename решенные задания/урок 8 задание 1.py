s1 = input('Введите слово: ')
s1 = s1.lower()
s2 = s1[len(s1)::-1]
if s1 == s2:
    print('yes')
else:
    print('no')