#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 126
Менеджеры контекста и инструкция with
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-16"

import os
import threading
from contextlib import contextmanager

dir_path = os.path.dirname(os.path.realpath(__file__))

# Инструкция with позволяет организовать выполнение последовательности
# инструкций внутри контекста, управляемого объектом, который играет
# роль менеджера контекста. Например
with open(os.path.join(dir_path, 'one-ten.txt')) as f:
    for line in f.readlines():
        print(f"line={line}", end='')

lock = threading.Lock()
with lock:
    # Начало критического блока
    # инструкции
    pass
    # Конец критического блока


class With_Test:
    """
    Тестирование инструкции with
    """

    def __enter__(self):
        """
        Данный метод вызвается когда интерпритатор встречает инструкцию with
        :return:
        """
        print(f'hello from __enter__.')
        return f"hello 'as var'"

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Данный метод вызывается когда интерпритатор покидает контекст
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        print(f"hello from __exit__, exc_type={exc_type}, exc_val={exc_val}, exc_tb={exc_tb}")
        return True  # True означает, что было обработано исключение
        # return False  # возникшее исключение продолжит свое движение вверх за пределами контекста

    def __init__(self):
        """
        Конструктор With_Test
        """
        print(f"конструктор With_Test")


print(f"")
wt = With_Test()
with wt as something:
    print(f"в контексте With_Test")
    print(f"something={something}")
    raise RuntimeError(
        "сгенерим ошибку")  # т.к. __exit__ у нас возвращает True, исключение не выйдет за пределы контекста with


class ListTransaction:
    def __init__(self, thelist):
        self.thelist = thelist

    def __enter__(self):
        self.workcopy = list(self.thelist)
        return self.workcopy

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.thelist[:] = self.workcopy
        return False


items = [1, 2, 3]
with ListTransaction(items) as working:
    working.append(4)
    working.append(5)
print(f"items={items}")

try:
    with ListTransaction(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError("сгенерим исключение")
except RuntimeError:
    pass
print(f"items={items}")


@contextmanager
def ListTransaction2(thelist):
    workingcopy = list(thelist)
    yield workingcopy
    # изменить оригинальный список, только если не возникло ошибок
    thelist[:] = workingcopy


items = [1, 2, 3]
with ListTransaction2(items) as working:
    working.append(4)
    working.append(5)
print(f"items={items}")

try:
    with ListTransaction2(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError("сгенерим исключение")
except RuntimeError:
    pass
print(f"items={items}")
print(f"__debug__={__debug__}")
try:
    assert False, 'пробуем ассерт'
except AssertionError as e:
    print(f"перехватили AssertationError e={e}")
except Exception as e:
    print(f"another exception has occurred e={e}")

