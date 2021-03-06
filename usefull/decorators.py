#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
decorators.py
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-17,2020-01-27"

from functools import wraps
import inspect
from datetime import datetime


def init_members(members):
    """
    Decorator for __init__ method of a class,
    it initializes members of an instance of a class with arguments passed to an __init__ method.
    E.g. __init__(x, y) will result in self.x = x; self.y = y; __init__(x, y)
    It can be used for any method, not only for __init__.
    Usage:

    class Something:
        @init_members
        def __init__(x, y, z):
            # @init_members will perform
            # self.x = x
            # self.y = y
            # self.z = z
            # before calling __init__(x, y, z) method
            pass


    class Something:
        @init_members(members=['x','z'])
        def __init__(x, y, z)
            # @init_members will perform
            # self.x = x
            # self.z = z
            # before calling __init__(x, y, z) method
            pass

    2020-01-17
    :param members: optional parameter, list of names of members to be initialized
    :return: decorated __init__ function
    """
    def wrapper(func):
        @wraps(func)
        def wrapped_f(self, *args, **kwargs):
            pass
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


def timer(func):
    """
    Decorator
    Runs function 'func', then prints the time of execution
    2020-01-27

    :param func:
    :return: func return
    """
    @wraps
    def wrapped_f(*args, **kwargs):
        start = datetime.now()
        return_value = func(*args, **kwargs)
        stop = datetime.now()
        print(f"'{func.__name__}' execution time='{stop-start}'")
        return return_value

    return wrapped_f

