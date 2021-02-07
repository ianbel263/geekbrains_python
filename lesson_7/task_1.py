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

MATRIX_SIZE = 5
LINE_SIZE = 6


def render_matrix():
    matrix_list = []
    for i in range(MATRIX_SIZE):
        line = []
        for j in range(LINE_SIZE):
            line.append(randint(0, 20))
        matrix_list.append(line)
    return matrix_list


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        result = ''
        for line in self.matrix_list:
            string = f'{"     ".join(map(lambda x: f"{str(x).rjust(2)}", line))}\n'
            result += string
        return result

    def __add__(self, other):
        result = []
        for i, line in enumerate(self.matrix_list):
            new_line = []
            for j, number in enumerate(line):
                new_line.append(number + other.matrix_list[i][j])
            result.append(new_line)
        return Matrix(result)


matrix_1 = Matrix(render_matrix())
matrix_2 = Matrix(render_matrix())
print('Исходная матрица №1: ', matrix_1, sep='\n')
print('Исходная матрица №2: ', matrix_2, sep='\n')
print('Полученная матрица: ', matrix_1 + matrix_2, sep='\n')
# добавить варианты сложения разных матриц
