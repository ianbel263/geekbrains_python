# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json


def read_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        return file.readlines()


def parse_data(data):
    firms_data = []
    firms_dict = {}
    profit_dict = {}
    profits = []
    for el in data:
        el = el.strip().split()
        profit = int(el[2]) - int(el[3])
        firms_dict[el[0]] = profit
        if profit > 0:
            profits.append(profit)

    profit_dict['average_profit'] = round(sum(profits) / len(profits))
    firms_data.append(firms_dict)
    firms_data.append(profit_dict)

    return firms_data


def write_json_file(data):
    with open('task_7.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)


write_json_file(parse_data(read_file('task_7.txt')))
