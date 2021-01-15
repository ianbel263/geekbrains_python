distance_first_day = int(input('Введите количество километров, которые пробежал спортсмен в первый день: '))
distance_arrive = int(input('Введите результат в километрах, которого должен достичь спортсмен: '))

days_count = 1

while True:
    days_count += 1
    distance_first_day += distance_first_day * 10 / 100
    if distance_first_day >= distance_arrive:
        break

print(f'на {days_count} день спортсмен достиг результата — не менее {distance_arrive} км')
