
def create(id):
    a1 = input('Введите имя питомца: ')
    a = input('Вид питомца: ')
    a2 = int(input('Возраст питомца: '))
    a3 = input('Имя владельца:  ')
    pets2 = {'Вид питомца:':a,'Возраст питомца: ':a2, 'Имя владельца:':a3}
    pets3[a1] = pets2
    print(pets2)
    print(pets3)
    pets[id] = pets3.copy()
    return

def read(id):
    print(pets[id])
    return
def update(id):
    create(id)
    return
def delete(id):
    pets.pop(id)
    return
def get_suffix(a2):
    y = ''
    if a2 % 10 == 1 and a2 != 11 and a2 % 100 != 11:
        y = 'год'
    elif 1 < a2 % 10 <= 4 and a2 != 12 and a2 != 13 and a2 != 14:
        y = 'года'
    else:
        y = 'лет'
    return y
# 
# 

pets = {}
pets2 = {}
pets3 = {}
tmp = {}
while (True):
    ffunc = input('''Введите команду :
                  create: Данная команда будет создавать новую запись с информацией о питомце
                  read: Данная команда будет отображать информацию о запрашиваемом питомце
                  update: Данная команда будет обновлять информацию об указанном питомце
                  delete: Данная команда будет удалять запись о существующем питомце
                  stop: Выход из программы
                  ''')
    if ffunc == 'stop':
        break
    elif ffunc == 'create':
        id = 0
        id = int(len(pets)+1)
        idtest = id in pets
        if idtest == False:
            create(id)
            print (pets)
            pets2.clear()
            pets3.clear()
        else:
            print(f'Животное с таким ID уже существует')
            continue
        
    elif ffunc == 'read':
        id = int(input('Введите id питомца: '))
        idtest = id in pets
        if idtest == True:
            read(id)            
        else:
            print(f'Животное с таким ID не существует')
            continue
       
    elif ffunc == 'update':
        id = int(input('Введите id питомца: '))
        idtest = id in pets
        if idtest == True:
            update(id)
            print (pets)
        else:
            print(f'Животное с таким ID не существует')
            continue
        
    elif ffunc == 'delete':
        id = int(input('Введите id питомца: '))
        idtest = id in pets
        if idtest == True:
            delete(id)
            print (pets)
        else:
            print(f'Животное с таким ID не существует')
            continue
    else:
        print('Неверная команда')