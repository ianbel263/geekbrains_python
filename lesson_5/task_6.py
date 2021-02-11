# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re


def read_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        return file.read().split('\n')


def create_lessons_dict(data):
    pattern_word = r'[А-Яа-я]+'
    pattern_hour_numbers = r'\d+'
    lessons_dict = {}
    for el in data:
        name_match = re.match(pattern_word, el)
        hour_numbers_matches = re.findall(pattern_hour_numbers, el)
        if name_match:
            name = name_match.group()
            hour_numbers = sum(map(int, hour_numbers_matches))
            lessons_dict[name] = hour_numbers
    return lessons_dict


print(create_lessons_dict(read_file('task_6.txt')))
