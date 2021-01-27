# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

# способ через словарь
seasons = {
    'зима': [1, 2, 12],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}

user_month = int(input('Введите номер месяца от 1 до 12: '))

for season, months in seasons.items():
    if user_month in months:
        print(f'Этот месяц относится к времени года - {season}')

# способ через список
seasons = [
    ['зима', 1, 2, 12],
    ['весна', 3, 4, 5],
    ['лето', 6, 7, 8],
    ['осень', 9, 10, 11]
]

user_month = int(input('Введите номер месяца от 1 до 12: '))
for season in seasons:
    if user_month in season:
        print(f'Этот месяц относится к времени года - {season[0]}')