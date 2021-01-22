# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

from task_2 import get_user_data


def pow_number(num_1, num_2):
    return num_1 ** num_2


def pow_number_cycle(num_1, num_2):
    result = 1
    i = 1
    while i <= abs(num_2):
        result *= num_1
        i += 1

    return 1 / result


degree_basis = get_user_data('Введите основание степени: ', is_int=True)
degree_power = get_user_data('Введите показатель степени (только отрицательное значение): ', is_int=True,
                             is_negative=True)

print('С помощью оператора "*":')
print(f'{degree_basis} в степени {degree_power} равно', pow_number(degree_basis, degree_power))
print()
print('С помощью цикла:')
print(f'{degree_basis} в степени {degree_power} равно', pow_number_cycle(degree_basis, degree_power))
