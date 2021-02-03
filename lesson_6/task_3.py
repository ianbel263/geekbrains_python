# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    name = None
    surname = None
    position = None

    _income = {}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


workers = []
manager = Position('Григорий', 'Пивоваров', 'менеджер', {'wage': 30000, 'bonus': 5000})
workers.append(manager)
cleaner = Position('Людмила', 'Васильева', 'уборщица', {'wage': 10000, 'bonus': 1000})
workers.append(cleaner)
director = Position('Василий', 'Петрович', 'директор', {'wage': 60000, 'bonus': 10000})
workers.append(director)

for worker in workers:
    print(worker.get_full_name(), worker.get_total_income(), sep=' - ')
