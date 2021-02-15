# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать
# формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc_weight(self, weight_per_metre, thickness):
        return self.__length * self.__width * weight_per_metre * thickness / 1000


try:
    road_length = int(input('Введите длину дороги в метрах: '))
    road_width = int(input('Введите ширину дороги в метрах: '))
    road_weight_per_metre = int(
        input('Введите массу асфальта для покрытия одного метра дороги толщиной 1 см в килограммах: '))
    road_thickness = int(input('Введите толщину полотна в сантиметрах: '))
except ValueError:
    print('Пожалуйста, вводите только числа')
    exit(1)
else:
    road = Road(road_length, road_width)
    print(f'Вам понадобится {road.calc_weight(road_weight_per_metre, road_thickness):.2f} тонн асфальта')
