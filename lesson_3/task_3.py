# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

from task_2 import get_user_data


def get_sum_two_max(num_1, num_2, num_3):
    """Возвращает сумму двух наибольших аргументов"""
    numbers = [num_1, num_2, num_3]
    min_num = min(numbers)
    numbers.remove(min_num)
    return sum(numbers)


user_num_1 = get_user_data('Введите первое число: ', is_int=True)
user_num_2 = get_user_data('Введите второе число: ', is_int=True)
user_num_3 = get_user_data('Введите третье число: ', is_int=True)

print('Сумма двух наибольших чисел равна', get_sum_two_max(user_num_1, user_num_2, user_num_3))
