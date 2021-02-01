# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint


def write_file(file_name, numbers):
    with open(file_name, 'w') as file:
        file.write(' '.join(map(lambda x: str(x), numbers)))


def create_numbers_list():
    numbers = []
    for number in range(21):
        numbers.append(randint(1, 100))
    return numbers


def read_file(file_name):
    with open(file_name) as file:
        return file.read().split()


def get_sum(numbers):
    return sum(map(lambda x: int(x), numbers))


write_file('task_5.txt', create_numbers_list())
print('Сумма всех числе в файле:', get_sum(read_file('task_5.txt')))
