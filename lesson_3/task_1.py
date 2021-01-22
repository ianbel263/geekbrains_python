# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div_int(num_1, num_2):
    """Возвращает частное от деления num_1 на num_2"""
    try:
        return round(num_1 / num_2, 2)
    except ZeroDivisionError:
        return 'На ноль делить нельзя'


user_number_1, user_number_2 = None, None
while user_number_1 is None or user_number_2 is None:
    try:
        user_number_1 = int(input('Введите делимое: '))
        user_number_2 = int(input('Введите делитель: '))
    except ValueError:
        print('Вы ввели не число')

print(f'Частное от деления {user_number_1} на {user_number_2} равно {div_int(user_number_1, user_number_2)}')
