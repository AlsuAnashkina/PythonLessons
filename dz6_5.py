# . Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
        print(f'Создана канцелярская принадлежность - {self.title}')

    def draw(self):
        print('Запуск отрисовки ')

class Pen(Stationery):
    def draw(self):
        print('Запсук отрисовки ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Запсук отрисовки карандашом')

class Handle(Stationery):
    def draw(self):
        print('Запсук отрисовки маркером')

pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw

