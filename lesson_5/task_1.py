# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

def save_user_data():
    with open('task_1.txt', 'a', encoding='utf-8') as file:
        while user_data := input('Введите данные для записи в файл (для выхода нажмите ENTER): '):
            file.write(user_data + '\n')


save_user_data()
