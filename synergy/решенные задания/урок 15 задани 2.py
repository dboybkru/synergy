class Transport:
   def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage    
class Autobus(Transport):
    def __init__(self, name, max_speed, mileage, seating_capacity):
        super().__init__(name, max_speed, mileage) #позволяет наследовать методы старшего класса
        self.seating_capacity = seating_capacity
    def __str__(self): #Метод для вывода информации об объекте класса (найден на просторах интернета)
        return f'Название автомобиля: {self.name}. Скорость: {str(self.max_speed)}. Пробег: {str(self.mileage)}. Вместимость {str(self.seating_capacity)}'
bus = Autobus('Renault Logan', 180 , 12, 50)
print(bus)