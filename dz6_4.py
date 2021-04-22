# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
# WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        print(f' создана машина {self.name}, {self.speed}, {self.color}, {self.is_police}')

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула {self.direction}')

    def show_speed(self, speed):
        self.speed = speed
        print(f'Текущая скорость автомобиля {self.speed}')

class TownCar(Car):

    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 60:
            print('Превышение скорости')
        else:
            print(f'Текущая скорость автомобиля {self.speed}')

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.is_police = True #????????????????????

class WorkCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print(f'Текущая скорость автомобиля {self.speed}')


work = WorkCar(80, 'синий', 'Трактор')
work.show_speed(80)
work.go()
work.stop()
work.turn('направо')

town = TownCar(60, 'красный', 'автобус')
town.go()
town.stop()
town.turn('налево')

police = PoliceCar(70, 'синий', 'Полиция')

