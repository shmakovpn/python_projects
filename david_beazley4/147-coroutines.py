#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 148
Сопрограммы
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-09"


import bz2
import fnmatch
import gzip
import os
import sys
#from asyncio import coroutine


def coroutine(func):
    def wrapper(*args, **kwargs):
        iterator = func(*args, **kwargs)
        next(iterator)
        return iterator
    return wrapper


@coroutine
def ssay():
    while True:
        x = (yield)
        print(f"x={x}")


# sayer = ssay()
# #next(sayer)
# sayer.send('hello')
# sayer.send('hello')
# sayer.send('hello')

@coroutine
def find_files(target):
    """
    2020-01-09
    :param target:
    :return:
    """
    while True:
        topdir, pattern = (yield)
        for path, dirname, filelist in os.walk(topdir):
            for name in filelist:
                if fnmatch.fnmatch(name, pattern):
                    target.send(os.path.join(path, name))


@coroutine
def opener(target):
    """
    2020-01-09
    :param target:
    :return:
    """
    while True:
        name = (yield)
        if name.endswith(".gz"):
            f = gzip.open(name)
        elif name.endswith(".bz2"):
            f = bz2.BZ2File(name)
        else:
            f = open(name, 'rb')
        target.send(f)


@coroutine
def cat(target):
    while True:
        f = (yield)
        for line in f:
            target.send(line)


@coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        str_line = line.decode()
        if pattern in str_line:
            target.send(str_line)


@coroutine
def printer():
    while True:
        line = (yield)
        sys.stdout.write(line)


finder = find_files(opener(cat(grep("wsgi", printer()))))
# Теперь передать значение
finder.send(('/var/log/apache2', 'access.log*'))
