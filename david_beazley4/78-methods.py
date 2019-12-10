#!/usr/bin/env python
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 76
Пользовательские функции
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-09"


class Foo:
    """
    Foo desc
    """
    def my_func(self, arg1='val1', arg2=None, *args, **kwargs):
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


x = Foo()
print(f"x.__doc__={x.__doc__}")

# аттрибуты методов
print(f"x.my_func.__doc__={x.my_func.__doc__}")
print(f"x.my_func.__name__={x.my_func.__name__}")
print(f"x.my_func.__class__={x.my_func.__class__}")
print(f"x.my_func.__func__={x.my_func.__func__}")
print(f"x.my_func.__self__={x.my_func.__self__}")


# аттрибуты пользовательских функций
# print(f"my_func.__dict__={my_func.__dict__}")
# print(f"my_func.__code__={my_func.__code__}")
# print(f"my_func.__defaults__={my_func.__defaults__}")
# print(f"my_func.__globals__={my_func.__globals__}")
# print(f"my_func.__closure__{my_func.__closure__}")

# Аттрибуты встроенных функций и методов
print(f"x.__init__.__doc__={x.__init__.__doc__}")
print(f"x.__init__.__name__={x.__init__.__name__}")
print(f"x.__init__.__self__={x.__init__.__self__}")
# Еще примеры
print(f"x.__str__.__doc__={x.__str__.__doc__}")
print(f"x.__repr__.__doc__={x.__repr__.__doc__}")


# Классы и экземпляры как вызываемые объекты
class Bar(object):
    """
    Bar desc
    """
    def __init__(self):
        """
        This function creates a new instance of Bar
        """
        print(f"Bar.__init__")

    def __call__(self, *args, **kwargs):
        """
        For using an instance of Bar as function
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: bool if success
        """
        print(f"Bar.__call__ args={args}; kwargs={kwargs}")
        return True


b = Bar()
b('go go', {'name': 'john', 'age': 132})
