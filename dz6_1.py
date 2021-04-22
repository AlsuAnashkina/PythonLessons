#  Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
#  и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
#  светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный)
#  составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
#  Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
#  Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
#  соответствующее сообщение и завершать скрипт

class TrafficLight:

    def __init__(self, color):
        self.__color = color
        print(f'появился {self.__color}')
    def running(self):
        if self.__color == 'red':
            self.__color = 'yellow'
            self.lasting = 2
        elif self.__color == 'yellow':
            self.__color = 'green'
            self.lasting = 8
        elif self.__color == 'green':
            self.__color = 'red'
            self.lasting = 7
        else:
            print('Ошибка')
        print(f'цвет светофора переключился на {self.__color}, он будет гореть {self.lasting} сек')

red = TrafficLight('red')
yellow = TrafficLight('yellow')
green = TrafficLight('green')
black = TrafficLight('black')

red.running()

yellow.running()

green.running()

black.running()





