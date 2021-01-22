# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def create_new_user(name=None, surname=None, birth_year=None, city=None, email=None, phone_number=None):
    return {
        'name': name,
        'surname': surname,
        'birth_year': birth_year,
        'city': city,
        'email': email,
        'phone_number': phone_number
    }


# следующая функция будет импортироваться в 3-е и 4-е задания
def get_user_data(message, is_int=False, is_negative=False):
    datum = None
    if is_int:
        while datum is None:
            try:
                datum = int(input(message))
                if is_negative:
                    while datum >= 0:
                        print('Надо ввести отрицательное число')
                        datum = int(input(message))
            except ValueError:
                print('Надо ввести число')
                datum = None
    else:
        datum = input(message)

    return datum


def parse_dict(data):
    print('Данные пользователя: ', end='')
    for key, value in data.items():
        print(f'{key} - {value} / ', end='')


if __name__ == '__main__':
    user_name = get_user_data('Введите имя пользователя: ')
    user_surname = get_user_data('Введите фамилию пользователя: ')
    user_birth_year = get_user_data('Введите год рождения пользователя: ', is_int=True)
    user_city = get_user_data('Введите город продивания пользователя: ')
    user_email = get_user_data('Введите email пользователя: ')
    user_phone_number = get_user_data('Введите номер телефона пользователя: ', is_int=True)

    parse_dict(create_new_user(name=user_name, surname=user_surname, email=user_email, birth_year=user_birth_year,
                               phone_number=user_phone_number, city=user_city))
