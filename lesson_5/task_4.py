# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.
import re

eng_to_rus = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}


def translate(word):
    return eng_to_rus[word]


def write_file(file_name, text):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(text)


pattern = r'[a-zA-Z]+'


def read_file(file_name):
    content = []
    with open(file_name) as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                translated_word = translate(match.group())
                content.append(re.sub(pattern, translated_word, line))
    return content


write_file('task_4_rus.txt', read_file('task_4_eng.txt'))
