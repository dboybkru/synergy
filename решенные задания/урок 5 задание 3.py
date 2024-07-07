x = float(input('Введите минимальную сумму инвестиций:'))
mike = float(input('Введите возможную сумму инвестиций Майкла:'))
ivan = float(input('Введите возможную сумму инвестиций Ивана:'))
if mike >= x and ivan >= x:
    print(2)
elif mike >= x and ivan < x:
    print('Майкл')
elif mike < x and ivan >= x:
    print('Иван')
else:
    print(0)
