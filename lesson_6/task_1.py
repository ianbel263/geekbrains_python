# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
# осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав
# экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    color = 'red'

    __previous_mode = None
    __colors = ['red', 'yellow', 'green']
    __timeouts = [7, 2, 10]
    __text_colors = ['\033[31m', '\033[33m', '\033[32m']
    __default_text_color = '\033[0m'

    def running(self, mode=0):
        try:
            if self.__previous_mode is None and mode != 0 or (mode - self.__previous_mode) > 1:
                self.__exit()
        except TypeError:
            pass
        self.__switch(mode)
        self.__previous_mode = mode

    def __switch(self, mode):
        def func():
            print(self.__text_colors[mode], self.__colors[mode], sep='')

        self.__set_timeout(self.__timeouts[mode], func)
        self.color = self.__colors[mode]

    def __exit(self):
        print(self.__default_text_color, 'Неправильный порядок режимов работы светофора', sep='')
        exit(1)

    @staticmethod
    def __set_timeout(timeout, cb):
        cb()
        for sec in range(timeout, 0, -1):
            print(sec)
            sleep(1)


traffic_light_1 = TrafficLight()
traffic_light_1.running(0)
traffic_light_1.running(1)
traffic_light_1.running(2)
