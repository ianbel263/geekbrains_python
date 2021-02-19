# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список
# выводится на экран.

class ListValueError(Exception):
    def __init__(self, txt):
        self.txt = txt


def check_element(el):
    try:
        return int(el)
    except ValueError:
        raise ListValueError('Этот список необходимо заполнять только целыми числами')


def create_list():
    numbers = []
    while user_data := input('Введите числа, для окончания ввода просто нажмите ENTER: '):
        try:
            user_data = check_element(user_data)
            numbers.append(user_data)
        except ListValueError as e:
            print(e)
    return numbers


print(create_list())
