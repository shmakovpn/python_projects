#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 80
Модули
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-10"


import re
print(f"re.compile={re.compile}")
print(f"re.__dict__.compile={re.__dict__['compile']}")

# Аттрибуты модуля
print(f"re.__dict__={re.__dict__}")  # Словарь, содержащий атрибуты модуля
print(f"re.__doc__={re.__dict__}")  # Строка документирования модуля
print(f"re.__name__={re.__dict__}")  # Имя модуля
print(f"re.__file__={re.__dict__}")  # Имя файла, откуда был загружен модуль
print(f"re.__path__={re.__dict__}")  # Полное имя пакета. Определен, только когда объект модуля ссылается на пакет

