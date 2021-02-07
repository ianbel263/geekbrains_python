# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

from random import randint


def render_matrix():
    matrix_list = []
    for i in range(randint(1, 10)):
        line = []
        for j in range(randint(1, 10)):
            line.append(randint(0, 100))
        matrix_list.append(line)
    return matrix_list


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        result = ''
        for line in self.matrix_list:
            string = f'{"     ".join(map(lambda x: f"{str(x).rjust(3)}", line))}\n'
            result += string
        return result

    def __add__(self, other):
        result = []
        big_matrix = self._sort_lists(self.matrix_list, other.matrix_list)[1]
        for i, line in enumerate(big_matrix):
            new_line = []
            try:
                big_line = self._sort_lists(self.matrix_list[i], other.matrix_list[i])[1]
                small_line = self._sort_lists(self.matrix_list[i], other.matrix_list[i])[0]
            except IndexError:
                result.append(big_matrix[i])
                continue
            for j, number in enumerate(big_line):
                try:
                    new_line.append(number + small_line[j])
                except IndexError:
                    new_line.append(number)
            result.append(new_line)
        return Matrix(result)

    @staticmethod
    def _sort_lists(list_1, list_2):
        return sorted([list_1, list_2], key=len)


matrix_1 = Matrix(render_matrix())
matrix_2 = Matrix(render_matrix())
print('Исходная матрица №1: ', matrix_1, sep='\n')
print('Исходная матрица №2: ', matrix_2, sep='\n')
print('Полученная матрица: ', matrix_1 + matrix_2, sep='\n')
