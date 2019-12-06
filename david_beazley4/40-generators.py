#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 40
Генераторы
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-06"
import time
import re


def countdown(n):
    print(f"Обратный отсчет")
    while n > 0:
        yield n  # генерирует значение n
        n -= 1


# example 1
c = countdown(5)
print(f"countdown={c}")  # c это объект генератора
print(f"{next(c)}")  # 5
print(f"{next(c)}")  # 4
print(f"{next(c)}")  # 3
print(f"{next(c)}")  # 2
print(f"{next(c)}")  # 1
try:
    print(f"{next(c)}")
except StopIteration as e:
    print(f"raised exception stop iteration type={e.args}, value={str(e.value)}, class={e.__class__}")

# example 2
for i in countdown(5):
    print(f"i={i}")


# страница 41
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


def grep(lines, searchtext):
    for line2 in lines:
        if searchtext in line2:
            yield line2


# Реализация последовательности команд “tail -f | grep python”
# на языке Python
syslog = tail(open("/var/log/syslog"))
pylines = grep(syslog, "python")
for line in pylines:
    print(f"line={line}", end='')
