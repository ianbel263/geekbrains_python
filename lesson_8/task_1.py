# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу
# полученной структуры на реальных данных.

import time


class Date:
    def __init__(self, date):
        date_list = self.parse(date.split('-'))
        self.day, self.month, self.year = date_list
        try:
            self.valid(date_list)
        except ValueError as e:
            print(e)

    def __str__(self):
        return f'{self.day:02}-{self.month:02}-{self.year}'

    @classmethod
    def parse(cls, date_list):
        return list(map(int, date_list))

    @staticmethod
    def valid(date_list):
        # метод распух)) я бы сделал по-другому, если бы не условие задачи, он был бы не статическим,
        # разбил бы его на две части
        day, month, year = date_list
        max_day = 31
        days_count = {
            28: [2],
            30: [4, 6, 9, 11]
        }
        msg_err = 'Неверно введены данные:'

        if year % 4 == 0 and month == 2:
            max_day = 29
        else:
            for key, value in days_count.items():
                if month in value:
                    max_day = key

        if year < 1000 or year > 2999:
            raise ValueError(msg_err)
        elif month < 1 or month > 12:
            raise ValueError(msg_err)
        elif day < 1 or day > max_day:
            raise ValueError(msg_err)

    @staticmethod
    def valid_2(date_list):
        # Второй способ, при котором метод parse не нужен (вызвать можно в конструкторе: self.valid_2(date_list))
        try:
            time.strptime('/'.join(date_list), '%d/%m/%Y')
        except ValueError:
            print('Invalid date!')


days = [
    '01-01-2020',
    '01-01-3020',
    '28-02-2020',
    '29-02-2020',
    '29-02-2021',
    '31-12-2020',
    '32-12-2020',
    '31-13-2020',
    '31-04-2020',
    '30-04-2020'
]

for day in days:
    print(Date(day))
    print()
