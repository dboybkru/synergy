str_where = 'hello world'
str_find = 'lo '

ind_where = 0
ind_find = 0
len_where = (len(str_where))
len_find = (len(str_find))

while ind_where <= len_where - len_find and ind_find < len_find:
    if str_where[ind_where + ind_find] == str_find[ind_find]:
        ind_find += 1
    else:
        ind_where += 1
        ind_find = 0

print(f'"{str_where}"')
print(f'"{str_find}"')
if ind_find == len_find:
    print(f'Такая подстрока есть. Начало с {ind_where + 1} символа')
else:
    print('Такой подстроки нет.')