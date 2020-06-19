"""
module_finder.py
This script creates modules index
todo change script description
"""
__author__ = 'shmakovpn <shmakovpn@yandex.ru>'
__date__ = '2020-06-19'

import os
import sys
import re
from typing import List


def paths():
    for path in sys.path:
        if os.path.isdir(path):
            yield path
        # todo add support for zip archives


def find_py(path):
    for item in os.listdir(path):
        if item.lower() == '__pycache__':
            continue
        item_path = os.path.join(path, item)
        if item_path.lower().endswith('.py'):
            yield item_path
        if os.path.isdir(item_path):
            for sub_item_path in find_py(item_path):
                yield sub_item_path
        # todo add support for zip archives


def read_py(path):
    with open(path, 'r') as f:
        for line in f:
            yield line.rstrip('\n')


def get_declaration(lines):
    declarations = {
        'var': re.compile(r'^(?P<name>[A-Za-z_][0-9A-Za-z_]*)\s*=\s*[^+*=/-]'),  # matches: name=value
        'def': re.compile(r'^def\s+(?P<name>[A-Za-z_][0-9A-Za-z_]*)'),  # matches: def somefunc
        'class': re.compile(r'^class\s+(?P<name>[A-Za-z_][0-9A-Za-z_]*)'),  # matches: class someclass
    }
    for line in lines:
        for declaration in declarations:
            matches = declarations[declaration].search(line)
            if matches:
                yield (declaration, matches.group('name'), line, )


def filter_declaration(search, declarations, case_insensitive=False):
    if case_insensitive:
        search = search.lower()
    for declaration in declarations:
        if (not case_insensitive and (search in declaration[1])) \
                or (case_insensitive and (search in declaration[1].lower())):
            yield declaration


if __name__ == '__main__':
    for item in paths():
        for item_py in find_py(item):
            for result in filter_declaration('StringIO', get_declaration(read_py(item_py))):
                print(f"result={result}")
