# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

from functools import reduce

MIN_SALARY = 20000


# Способ 1
def calc_salary():
    print(f'Список сотрудников, имеющих оклад менее {MIN_SALARY} рублей:')
    with open('task_3.txt', encoding='utf-8') as file:
        sum_salary = 0
        for i, line in enumerate(file):
            line = line.strip().split()
            salary = int(line[1])
            print(line[0]) if salary < MIN_SALARY else None
            sum_salary += salary

    print(f'Средняя величина дохода сотрудников составляет {sum_salary / (i + 1):.2f} рублей.')


calc_salary()

print()
print()


# Способ 2
def read_file():
    with open('task_3.txt', encoding='utf-8') as file:
        return file.readlines()


def find_employees_less_then_min_salary(data):
    data = list(map(lambda x: x.strip().split(), data))
    data.sort()
    data = filter(lambda x: int(x[1]) < MIN_SALARY, data)
    print(f'Список сотрудников, имеющих оклад менее {MIN_SALARY} рублей:')
    for name, salary in data:
        print(name)


def calc_salary(data):
    data = list(map(lambda x: x.strip().split(), data))
    print(
        f'Средняя величина дохода сотрудников составляет '
        f'{reduce(lambda acc, salary: acc + salary, map(lambda x: int(x[1]), data)) / len(data):.2f} '
        f'рублей.'
    )


find_employees_less_then_min_salary(read_file())
calc_salary(read_file())

# Алексей, подкажите, пожалуйста, какие способы предпочительней? Имеет смысл пробегаться по
# файлу несколько раз map()-ами, reduce()-ами и т.д., как во втором способе, или есть еще более лучшие варианты?
