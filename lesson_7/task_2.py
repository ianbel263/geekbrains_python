# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    __fabric_consumptions = []

    def __init__(self, client):
        self.client = client

    def add_clothes(self, clothes_type, clothes_size):
        if clothes_type == 'coat':
            clothes = Coat(clothes_size)
        elif clothes_type == 'suit':
            clothes = Suit(clothes_size)
        else:
            print(f'Неверно введен тип одежды: {clothes_type}')
            return
        self.__fabric_consumptions.append(clothes.calc_fabric_consumption)

    @property
    def calc_fabric_consumption(self):
        return sum(self.__fabric_consumptions)


class Coat:
    def __init__(self, size):
        self.size = size

    @property
    def calc_fabric_consumption(self):
        return round(self.size / 6.5 + 0.5)


class Suit:
    def __init__(self, height):
        self.height = height

    @property
    def calc_fabric_consumption(self):
        return round(2 * self.height + 0.3)


clothes_ivanov = Clothes('Ivanov')
clothes_ivanov.add_clothes('coat', 20)
clothes_ivanov.add_clothes('suit', 10)
print(f'Общий расход ткани: {clothes_ivanov.calc_fabric_consumption}')
