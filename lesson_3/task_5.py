# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter
# должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
# и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.

def remove_not_int(data):
    """Удаляет все элементы списка, которые нельзя привести к int"""
    data_list = data.split()
    is_not_int = False

    for i, el in enumerate(data_list):
        try:
            data_list[i] = int(el)
        except ValueError:
            is_not_int = True

    if is_not_int:
        numbers = [datum for datum in data_list if type(datum) is int]
    else:
        numbers = data_list

    return numbers


def check_exit_key(data):
    if 'y' in data:
        return True


total = 0
is_exit_symbol_enter = False

while not is_exit_symbol_enter:
    user_data = input('Введите строку чисел, разделенных пробелами (для выхода из программы введите "y"): ')
    total += sum(remove_not_int(user_data))
    is_exit_symbol_enter = check_exit_key(user_data)

    print('Сумма:', total)
