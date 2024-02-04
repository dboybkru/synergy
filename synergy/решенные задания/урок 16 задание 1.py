class Kassa(object):
    kassa = 0
    def top_up(self,x):
        Kassa.kassa += x
        print('Баланс: ', Kassa.kassa)
    def take_away(self,x):
        Kassa.kassa -= x
        print('Баланс: ', Kassa.kassa)
    def count(self):
        print(Kassa.kassa//1000)
x=0        
kassa = Kassa()
while (True):    
    y = input('''
    Введите UP для пополнения:
    Введите Away для снятия:
    Введите Count что бы узанать сколько целых тысяч осталось в кассе:
    Введите Quit для выхода:''')
    if y == 'UP':
        x = int(input('Введите сумму:'))
        kassa.top_up(x)
    elif y == 'Away':
        x = int(input('Введите сумму:'))
        kassa.take_away(x)
    elif y == 'Count':
        kassa.count
    elif y == 'Quit':
        break
    
