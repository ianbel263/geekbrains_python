# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def calc_payroll(output_in_hours, rate_per_hour, bonus):
    return output_in_hours * rate_per_hour + bonus


try:
    script_name, param_1, param_2, param_3 = argv
    print('Размер заработной платы составит:', calc_payroll(int(param_1), int(param_2), int(param_3)))
except ValueError:
    print('Надо передать три параметра')
