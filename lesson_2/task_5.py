# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

import random

rank_list = []
for number in range(random.randint(10, 20)):
    rank_list.append(random.randint(0, 10))

rank_list.sort(reverse=True)
print(f'Исходный список: {rank_list}')

user_number = int(input('Введите натуральное число: '))

if user_number >= max(rank_list):
    rank_list.insert(0, user_number)
elif user_number <= min(rank_list):
    rank_list.append(user_number)
else:
    for i in range(1, len(rank_list)):
        if user_number in (range(rank_list[i], rank_list[i - 1])):
            rank_list.insert(i, user_number)
            break

print(f'Результат: {rank_list}')
