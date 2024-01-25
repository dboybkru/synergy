class Transport(object):    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def display_info(self):
        print(f'Название автомобиля: {self.name}. Скорость: {str(self.max_speed)}. Пробег: {str(self.mileage)}.')   
autobus = Transport('Renault Logan', 180 , 12)
autobus.display_info()


