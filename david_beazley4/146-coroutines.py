#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Книга Девида Бизли "Python подробный справочник 4ое издание"
страница 146
Сопрограммы
"""
__author__ = "shmakovpn <shmakovpn@yandex.ru>"
__date__ = "2020-01-09"


import os
import sys
import fnmatch  # Filename matching with shell patterns.
import gzip, bz2


def find_files(topdir, pattern):
    """
    Герератор
    Находит файлы в topdir шаблону pattern
    2020-01-09
    :param topdir: корневая директория для поиска файлов
    :param pattern: шаблон для находимых файлова
    :return: путь к найденному файлу
    """
    for path, dirname, filelist in os.walk(topdir):
        for name in filelist:
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(path, name)  # возвращаем полный путь к файлу


def opener(filenames):
    """
    Герератор
    Открывает файлы из списка filenames и возвращает открытый файл
    2020-01-09
    :param filenames: список путей к файлам или итератор выдающий полный путь к файлу
    :return: объект открытого файла
    """
    for name in filenames:
        print(f"opening f={name}")
        if name.endswith(".gz"):
            f = gzip.open(name)
        elif name.endswith(".bz2"):
            f = bz2.BZ2File(name)
        else:
            f = open(name, 'rb')
        yield f


def cat(filelist):
    """
    Генератор
    Выводит строки из файлов из списка filelist
    2020-01-09
    :param filelist: список объектов открытых файлов
    :return: строка из файла
    """
    for f in filelist:
        for line in f:
            yield line


def grep(pattern, lines):
    """
    Генератор
    Возращает строки соотвествующие шаблону из списка строк
    2020-01-09
    :param pattern: шаблон для фильтрации строк
    :param lines: список строк
    :return: строка соотстветствующая шаблону
    """
    for line in lines:
        str_line = line.decode()
        if pattern in str_line:
            yield str_line


wwwlogs = find_files('/var/log/apache2/', 'access.log*')
files = opener(wwwlogs)
lines = cat(files)
pylines = grep("wsgi", lines)
for line in pylines:
    sys.stdout.write(line)

