#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 130
функции
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2019-12-16"


def add(x, y):
    return x + y


print(f"add(2,3)={add(2, 3)}")

x = [1, 2, 3]


def test_args(arg):
    print(f"arg is {arg is x}")


test_args(x)

xx = (x,)

print(f"xx={xx}")

x.append(4)
print(f"xx={xx}")


def foo(x, items=[]):
    items.append(x)
    return items


print(f"foo(1)={foo(1)}")
print(f"foo(1)={foo(2)}")
print(f"foo(1)={foo(3)}")  # аргумент по умолячиню запоминает изменения в результате предыдущих вызовов


# поэтому следует избегать изменяемых объектов в качестве аргументов по умолчанию

def countdown(start):
    n = start

    def display():  # Объявление вложенной функции
        print('T-minus %d' % n)

    while n > 0:
        display()
        n -= 1


countdown(4)


def callfunc(func):
    return func()


def hello():
    return "hello"


print(f"{callfunc(hello)}")


def page(url):
    def get():
        print(f"get url={url}")

    return get


python = page('python')
jython = page('jython')

python()
jython()


# Замыкание может быть весьма эффективным способом сохранения инфор-
# мации о состоянии между вызовами функции. Например, рассмотрим сле-
# дующий пример, в котором реализован простой счетчик:
def countdown2(n):
    def next1():
        nonlocal n
        r = n
        n -= 1
        return r

    return next1


# Пример использования
next1 = countdown2(10)
while True:
    v = next1()  # Получить следующее значение
    print(f"v={v}")
    if not v: break


def trace(func):
    def callf(*args, **kwargs):
        print(f"Вызов {func.__name__}({args}, {kwargs})")
        r = func(*args, **kwargs)
        print(f"функция {func.__name__} вернула {r}")
        return r

    return callf


print(f"")
trace_test = trace(add)
trace_test(3, 4)
print(f"")


@trace
def test_decorator(a, b):
    print(f"test_decorator called a={a}, b={b}")
    return 'ok'


test_decorator('xx', 'yy')


# пример декоратора с аргументами
def trace_param(flag):
    def register_func(func):
        print(f"Вызов {func.__name__} with flag={flag}")
        return func

    return register_func


print(f"")
trace_param_temp = trace_param("xxx")
trace_param_add = trace_param_temp(add)
trace_param_add(7, 8)
print(f"")


@trace_param(flag="YYY")
def test_flag(a, m):
    print(f"test flag a={a}, m={m}")


test_flag(5, 6)

# Декоратор обработчика события
# event_handlers = {}
# def event_handler(event):
#     def register_funcition
