# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

def calc_file_data():
    with open('task_2.txt', encoding='utf-8') as file:
        data = file.readlines()

    for i, line in enumerate(data):
        print(f'Количество слов в строке номер {i+1:3}: {len(line.split()):3}')
    print()
    print('Общее количество строк в файле:', len(data))


calc_file_data()
