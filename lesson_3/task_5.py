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


def check_exit_key(data):
    if 'y' in data:
        return True


total = 0
is_exit_symbol_enter = False

while not is_exit_symbol_enter:
    user_data = input('Введите строку чисел, разделенных пробелами (для выхода из программы введите "y"): ')
    total += sum(replace_not_int(user_data))
    is_exit_symbol_enter = check_exit_key(user_data)

    print('Сумма:', total)
