distance_first_day = int(input('Введите количество километров, которые пробежал спортсмен в первый день: '))
distance_arrive = int(input('Введите результат в километрах, которого должен достичь спортсмен: '))

days_count = 1

while distance_first_day < distance_arrive:
    days_count += 1
    distance_first_day += distance_first_day * 10 / 100
    print(f'{days_count} - {distance_first_day}')

print(f'на {days_count} день спортсмен достиг результата — не менее {distance_arrive} км')
