# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    title = None

    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисую ручкой под названием', self.title)


class Pencil(Stationery):
    def draw(self):
        print('Рисую карандашом под названием', self.title)


class Handle(Stationery):
    def draw(self):
        print('Рисую маркером под названием', self.title)


bic_pen = Pen('Bic')
kohinoor_pencil = Pencil('Kohinoor')
edding_marker = Handle('Edding')

bic_pen.draw()
kohinoor_pencil.draw()
edding_marker.draw()
