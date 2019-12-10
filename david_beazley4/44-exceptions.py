#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 44
Исключения
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-09"
import threading


try:
    f = open('does_not_exist.txt', 'r')
except IOError as e:
    print(f"error={str(e)}")


try:
    raise RuntimeError(f"hello from raise")
except RuntimeError as e:
    print(f"error={str(e)}")


# пример программного кода, который использует мьютекс в качестве блокировки
message_lock = threading.Lock()
messages = []

with message_lock:
    messages.append(f"new message")

