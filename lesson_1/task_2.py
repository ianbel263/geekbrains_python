user_time = int(input('Введите время в секундах: '))

time_hour = user_time // 3600
time_min = user_time % 3600 // 60
time_sec = user_time % 3600 % 60

print(f'{user_time} секунд это {time_hour:02}:{time_min:02}:{time_sec:02}')
