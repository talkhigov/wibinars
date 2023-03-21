class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.is_police = is_police
        self.speed = speed
    
    def show(self):
        print(f'Название: {self.name}\nЦвет: {self.color}\nТекущая Скорость: {self.speed}\nПолицейская: {self.is_police}')

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self):
        print(f'{self.name} повернула направо')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}км')

class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Вы превысили скорость!')
        else:
            print(f'Текущая скорость автомобиля {self.name}: {self.speed}км')

class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость!')
        else:
            print(f'Текущая скорость автомобиля {self.name}: {self.speed}км')

class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

solaris = TownCar('Hyundai solaris', 'white', 50, None)
solaris.show_speed()
solaris.show()
bmw = SportCar('BMW m5f90 cs', 'blue', 110, None)
bmw.show()
bmw.show_speed()
mercedes = PoliceCar('e63 amg', 'black', 200, True)
mercedes.show_speed()
print(mercedes.is_police)