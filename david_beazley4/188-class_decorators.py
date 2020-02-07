#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 188
Декораторы классов
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-27"


# декоратор класса - это функция, которая принимает и возвращает класс
registry = {}
def register(cls):
    registry[cls.__clsid__] = cls
    return cls

@register
class Foo:
    __clsid__ = "123-456"
    def bar(self):
        pass


from datetime import datetime
from functools import wraps


def timer(func):
    """
    Decorator
    Runs function 'func', then prints the time of execution
    2020-01-27

    :param func:
    :return: func return
    """
    @wraps(func)
    def wrapped_f(*args, **kwargs):
        start = datetime.now()
        return_value = func(*args, **kwargs)
        stop = datetime.now()
        print(f"'{func.__name__}' execution time='{stop-start}'")
        return return_value

    return wrapped_f


@timer
def some():
    from time import sleep
    sleep(1)


some()


# __slots__ и наследование
class SlotTestBase:
    __slots__ = ('a', 'b',)

    def __init__(self):
        pass


class SlotTest(SlotTestBase):
    pass


st = SlotTest()
st.a = 'hello'
st.b = 'some'
st.c = 'gob'  # it works
print(f"st.__slots__={st.__slots__}")

stb = SlotTestBase()
try:
    stb.x = 'test'
except AttributeError as e:
    print(f"e={e}")  # AttributeError: 'SlotTestBase' object has no attribute 'x'


class SlotTest2(SlotTestBase):
    __slots__ = SlotTestBase.__slots__ + ('c', 'd')

    def __init__(self):
        super().__init__()


st2 = SlotTest2()
st2.a = 'hello a'
st2.b = 'hello b'
st2.c = 'hello c'
st2.d = 'hello d'
try:
    st2.x = 'fail'
except AttributeError as e:
    print(f"e={e}")  # AttributeError: 'SlotTest2' object has no attribute 'x'


class SlotTest3(SlotTestBase):
    def __init__(self):
        self.__slots__ = super().__slots__ + ('c', 'd', )
        super().__init__()


st3 = SlotTest3()
st3.a = 'hello a'
st3.b = 'hello b'
st3.c = 'hello c'
st3.d = 'hello d'
st3.x = 'hello x'  # it works


class SlotTest4:
    __slots__ = SlotTest.__slots__ + ('c', 'd', )


st4 = SlotTest4()
st4.a = 'hello a'
st4.b = 'hello b'
st4.c = 'hello c'
st4.d = 'hello d'
try:
    st4.x = 'hello x'  # it works
except AttributeError as e:
    print(f"e={e}")  # AttributeError: 'SlotTest4' object has no attribute 'x'

# Вывод: __slots__ не наследуется


