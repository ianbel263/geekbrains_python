# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter
# должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
# и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.

def replace_not_int(data):
    """Заменяет нулями все элементы, которые нельзя привести к int"""
    data_list = data.split()

    for i, el in enumerate(data_list):
        try:
            data_list[i] = int(el)
        except ValueError:
            data_list[i] = 0

    return data_list


def check_exit_key(data=None):
    if data is None:
        data = []
    return True if EXIT_KEY in data else False


EXIT_KEY = 'y'
total = 0
user_data = None

while not check_exit_key(user_data):
    user_data = input(f'Введите строку чисел, разделенных пробелами (для выхода из программы введите {EXIT_KEY}): ')
    total += sum(replace_not_int(user_data))

    print('Сумма:', total)
