#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 41
Сопрограммы
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-06"
import time


# следит за содержимым файла (на манер команды tail -f)
def tail(f):
    """
    # Аналог tail -f
    :param f: дескриптор файла
    :return:
    """
    f.seek(0, 2)  # Переход в конец файла
    while True:
        line1 = f.readline()  # Попытаться прочитать новую строку текста
        if not line1:  # Если ничего не прочитано,
            time.sleep(0.1)  # приостановиться на короткое время
            continue  # и повторить попытку
        yield line1


def print_matches(match_text):
    print(f"поиск подстроки {match_text}")
    while True:
        line = (yield)  # получение текстовой строки
        if match_text in line:
            print(f"line={line}", end='')


matcher = print_matches("python")
next(matcher)  # Перемещение до первой инструкции (yield)
matcher.send("hello world")
matcher.send("python is cool")
matcher.send("yow!")
matcher.close()  # Завершение работы с объектом matcher

# совместное использование генератора и сопрограммы
# Множество сопрограмм поиска
matchers = [
    print_matches("python"),
    print_matches("guido"),
    print_matches("jython"),
]

# Подготовка всех подпрограмм к последующему вызову метода next()
for m in matchers:
    next(m)

# Передать активный файл журнала всем сопрограммам.
syslog = tail(open("/var/log/syslog"))
for line in syslog:
    for m in matchers:
        m.send(line)  # Передача данных каждой из сопрограмм


