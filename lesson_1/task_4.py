user_number = input('Введите целое положительное число: ')

i = 0
max_digit = user_number[0]

while i < len(user_number):
    if user_number[i] > max_digit:
        max_digit = user_number[i]
    i += 1

print(f'Максимальная цифра в числе {user_number}: {max_digit}')

# другой способ
print(f'С использованием функции max(): {max(user_number)}')
