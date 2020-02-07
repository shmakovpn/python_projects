#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 175
Управление памятью объектов (как работает удаление объектов)
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-17"

from functools import wraps
import inspect


def init_members(members):
    """
    Decorator for __init__ method of a class,
    it initializes members of an instance of a class with arguments passed to an __init__ method.
    E.g. __init__(x, y) will result in self.x = x; self.y = y; __init__(x, y)
    It can be used for any method, not only for __init__.
    2020-01-17
    :param members: optional parameter, list of names of members to be initialized
    :return: decorated __init__ function
    """
    def wrapper(func):
        @wraps(func)
        def wrapped_f(self, *args, **kwargs):
            func_args = inspect.getfullargspec(func).args[
                        1:]  # takes list of arguments of method 'func' without 'self'
            init_dict = {}
            # defaults
            func_defaults = list(inspect.getfullargspec(func).defaults)
            func_defaults.reverse()
            func_args_copy = list(func_args)
            for default_value in func_defaults:
                init_dict[func_args_copy.pop()] = default_value
            del func_args_copy
            del func_defaults
            # args
            args_list = list(args)
            for arg in args_list:
                init_dict[func_args.pop(0)] = arg
            del args_list
            # kwargs
            for kwarg in kwargs:
                if kwarg in func_args:
                    init_dict[kwarg] = kwargs[kwarg]
                    func_args.remove(kwarg)
            # clear
            del func_args
            # initialize members of 'self'
            if callable(members):
                for member_name in init_dict:
                    setattr(self, member_name, init_dict[member_name])
            else:
                for member_name in init_dict:
                    if member_name in members:
                        setattr(self, member_name, init_dict[member_name])
            return func(self, *args, **kwargs)

        return wrapped_f

    if callable(members):
        func = members
        return wrapper(func)
    return wrapper


class Complex:
    @init_members
    def __init__(self, real, imag=0):
        pass

    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"

    def __str__(self):
        return f"({self.real:g}+{self.imag:g}j)"

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)


c = Complex(2, 3)
print(f"str(Complex(2, 3))={str(Complex(2,3))}")
print(f"repr(Complex(2, 3))={repr(Complex(2,3))}")
print(f"Complex(2, 3)+4.0={Complex(2, 3)+4.0}")
try:
    x = 4.0 + c
except TypeError as e:
    print(f"e={e}")


class Complex2(Complex):
    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return Complex(other.real - other.real, other.imag - other.imag)


c2 = Complex2(2, 3)
print(f"Complex2(2,3)={Complex2(2,3)}")
