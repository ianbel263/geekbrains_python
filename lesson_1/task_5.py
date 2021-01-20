company_income = int(input('Введите прибыль фирмы: '))
company_costs = int(input('Введите издержки фирмы: '))

if company_income > company_costs:
    print('Фирма работает с прибылью')
    company_profit = company_income - company_costs
    profitability = round(company_profit / company_income * 100, 2)
    print(f'Рентабельность фирмы составляет: {profitability}%')
    staff_number = int(input('Введите численность сотрудников фирмы: '))
    profit_per_staff = round(company_profit / staff_number, 2)
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет: {profit_per_staff}')
elif company_income < company_costs:
    print('Фирма работает в убыток')
else:
    print('Фирма работает в ноль')
