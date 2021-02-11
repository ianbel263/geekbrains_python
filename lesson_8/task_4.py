# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

TEXT_COLORS = {
    'normal': '\033[37m',
    'warning': '\031[37m',
    'success_add': '\032[37m',
    'success_issue': '\033[37m',
}

class Warehouse:
    def __init__(self, name):
        self.name = name
        self._products = {}

    def print_all_products(self):
        for key, value in self._products.items():
            print(f'{key}:')
            for el in value:
                print(el)

    def add_product(self, product, count: int):
        if not isinstance(count, int):
            print(TEXT_COLORS['warning'] + 'Количество товара надо вводить только целыми числами')
            return
        if product.category in self._products.keys():
            for el in self._products[product.category]:
                if el['article_number'] == product.article_number and el['name'] == product:
                    el['count'] += count
                    return
                elif el['article_number'] == product.article_number and el['name'] != product:
                    print(f'Неверно введен артикул товара: {product.name}')
                    print(f'артикулу: {product.article_number} соответствует товар:\n{el["name"]}')
                    print('Товар на склад не добавлен\n')
                    return

        self._products.setdefault(product.category, []).append({
            'article_number': product.article_number,
            'name': product,
            'price': product.price,
            'count': count
        })

    def issue_product(self, product, count: int):
        if product.category not in self._products.keys():
            print('Такого товара на склвде нет\n')
            return

        for el in self._products[product.category]:
            if el['article_number'] == product.article_number:
                if el['count'] > count:
                    el['count'] -= count
                    break
                elif el['count'] == count:
                    self._products[product.category].remove(el)
                    print('Товар полностью удален со склада')
                    break
                else:
                    print('Такого количества товара на складе нет')
                    print(f'Остаток товара: {el["count"]}')
                    break
            else:
                print('Такого товара на склвде нет\n')


class Equipment:
    def __init__(self, article_number, name, color, price):
        self.article_number = article_number
        self.name = name
        self.color = color
        self.price = price
        self.category = f'{self.__class__.__name__}s'

    def __repr__(self):
        return f'{self.name}/{self.color}'

    def __str__(self):
        return f'Наименование: {self.name}\nЦена:{self.price}\nКатегория:{self.category}'


class Printer(Equipment):
    def __init__(self, article_number, name, color, price, print_speed):
        super().__init__(article_number, name, color, price)
        self.print_speed = print_speed


class Copier(Equipment):
    def __init__(self, article_number, name, color, price, is_multifunctional):
        super().__init__(article_number, name, color, price)
        self.is_multifunctional = is_multifunctional


class Scanner(Equipment):
    def __init__(self, article_number, name, color, price, scanner_type):
        super().__init__(article_number, name, color, price)
        self.scanner_type = scanner_type


warehouse_moscow = Warehouse('Moscow')
printer_brother = Printer(1, 'Brother', 'white', 8000, 20)
printer_hp = Printer(2, 'HP', 'black', 10000, 15)
printer_hp_2 = Printer(1, 'HP', 'black', 10000, 15)
scanner_canon = Scanner(3, 'Canon', 'black', 5000, 'tablet')
copier_xerox = Copier(4, 'Xerox', 'silver', 9000, True)

warehouse_moscow.issue_product(printer_brother, 15)

warehouse_moscow.add_product(printer_brother, 'sasa')
warehouse_moscow.add_product(printer_brother, 10)
warehouse_moscow.add_product(printer_brother, 10)
warehouse_moscow.add_product(printer_brother, 10)
warehouse_moscow.add_product(printer_hp, 10)
warehouse_moscow.add_product(printer_hp_2, 10)
warehouse_moscow.add_product(scanner_canon, 5)
warehouse_moscow.add_product(scanner_canon, 5)
warehouse_moscow.add_product(printer_hp, 5)

warehouse_moscow.print_all_products()
print()
warehouse_moscow.issue_product(printer_brother, 17)
warehouse_moscow.issue_product(printer_brother, 9)
warehouse_moscow.issue_product(printer_brother, 3)
warehouse_moscow.issue_product(printer_brother, 1)
warehouse_moscow.issue_product(printer_brother, 1)
print()
warehouse_moscow.print_all_products()
