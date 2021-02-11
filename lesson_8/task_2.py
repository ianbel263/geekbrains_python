# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class DivisionByZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div_int(divisible, privat):
    if privat == 0:
        raise DivisionByZeroError('На нуль делить нельзя!')
    return divisible / privat


user_divisible = int(input('Введите делимое: '))
user_privat = int(input('Введите делитель: '))

try:
    print('Результат деления:', div_int(user_divisible, user_privat))
except DivisionByZeroError as e:
    print(e)
