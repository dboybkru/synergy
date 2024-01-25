class Transport:
   def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        #super().__init__(name, max_speed, mileage) Можно использоваь, но в уроке данный приём не рассмотрен, позволяет наследовать методы старшего класса
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def __str__(self): #Метод для вывода информации об объекте класса (найден на просторах интернета)
        return f'Название автомобиля: {self.name}. Скорость: {str(self.max_speed)}. Пробег: {str(self.mileage)}.'
bus = Autobus('Renault Logan', 180 , 12)
print(bus)


