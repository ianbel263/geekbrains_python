# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    name = ''
    color = ''
    is_police = False

    speed = 0
    direction = 0

    _acceleration_factor = 1
    _directions = ['left', 'right']

    def __init__(self, name, color, is_police):
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self):
        self.speed = round(self.speed + 1 * self._acceleration_factor, 2)
        if round(self.speed) == 0:
            self.speed = 0

    def stop(self):
        self.speed = round(self.speed - 1, 2)
        if round(self.speed) == 0:
            self.speed = 0

    def turn(self, direction):
        if direction == self._directions[0]:
            self.direction = self.direction - 15 if abs(self.direction - 15) < 360 else 0
        elif direction == self._directions[1]:
            self.direction = self.direction + 15 if self.direction + 15 < 360 else 0

    def show_speed(self):
        return self.speed

    def show_direction(self):
        return self.direction

    def get_going(self):
        if self.speed == 0:
            return 'Машина стоит'
        elif self.speed > 0:
            return 'Машина едет вперед'
        else:
            return 'Машина едет назад'

    def get_direction(self):
        if self.direction == 0:
            return 'Руль повернут в прямом направлении'
        elif self.direction > 0:
            return 'Руль повернут направо'
        else:
            return 'Руль повернут налево'


class TownCar(Car):
    _speed_limit = 60

    def show_speed(self):
        if self.speed > self._speed_limit:
            print('Превышение скорости')
        return self.speed


class WorkCar(Car):
    _speed_limit = 40
    _acceleration_factor = 0.9

    def show_speed(self):
        if self.speed > self._speed_limit:
            print('Превышение скорости')
        return self.speed


class SportCar(Car):
    _acceleration_factor = 1.2


class PoliceCar(Car):
    is_police = True
    _acceleration_factor = 1.1


kia = TownCar('Kia', 'silver', False)
mazda = TownCar('Mazda', 'black', False)
tractor = WorkCar('JCB', 'yellow', False)
porsche = SportCar('Porsche', 'blue', False)
ford = PoliceCar('Ford', 'white', True)


def get_car_parameters(car):
    print(car.get_going())
    print('Скорость равна', abs(car.show_speed()))
    print(car.get_direction())
    print('Угол поворота:', car.show_direction())


def drive_car(car):
    while user_key := input(': '):
        if user_key == 'w':
            car.go()
            get_car_parameters(car)
        elif user_key == 's':
            car.stop()
            get_car_parameters(car)
        elif user_key == 'a':
            car.turn('left')
            get_car_parameters(car)
        elif user_key == 'd':
            car.turn('right')
            get_car_parameters(car)


print('Для выхода нажмите ENTER дважды')
print('Для движения вперед введите w')
print('Для движения торможения/движения назад введите s')

drive_car(porsche)

# что-то соорудил) я не стал пока разбираться с обработчиками событий, сделал пока так, правда получилось
# странное поведение руля - он крутится по кругу)
