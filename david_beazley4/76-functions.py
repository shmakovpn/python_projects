#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 76
Пользовательские функции
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-09"


def my_func(arg1='val1', arg2=None, *args, **kwargs):
    """
    About my function
    :param arg1: desc1
    :param arg2: desc2
    :param args: positional arguments
    :param kwargs: keyword arguments
    :return: some value
    """
    print(f"arg1={arg1}")
    print(f"arg2={arg2}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")
    return True


print(f"my_func.__doc__={my_func.__doc__}")
print(f"my_func.__name__={my_func.__name__}")
print(f"my_func.__dict__={my_func.__dict__}")
print(f"my_func.__code__={my_func.__code__}")
print(f"my_func.__defaults__={my_func.__defaults__}")
print(f"my_func.__globals__={my_func.__globals__}")
print(f"my_func.__closure__{my_func.__closure__}")
