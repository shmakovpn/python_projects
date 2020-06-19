"""
test_module_finder.py
tests for module_finder.py
"""
__author__ = 'shmakovpn <shmakovpn@yandex.ru>'
__date__ = '2020-06-19'

import unittest
from .module_finder import filter_declaration


class TestModuleFinder(unittest.TestCase):
    def test_filter_declaration(self):
        declaration_strings = (
            ('var', 'hello', 'hello = [1, 2, 3, ]', ),
            ('class', 'Car', 'class Car(Vehicle):', ),
            ('def', 'sing', 'def sing(song):',),
            ('def', 'get_car', 'def get_car(cars):', ),
        )
        search_query = 'Car'
        search_results = list(filter_declaration(search=search_query, declarations=declaration_strings))
        self.assertEqual(len(search_results), 1)
        self.assertEqual(search_results[0], declaration_strings[1])
        search_results_case_insensitive = list(filter_declaration(search_query, declaration_strings, case_insensitive=True))
        self.assertEqual(len(search_results_case_insensitive), 2)
        self.assertEqual(search_results_case_insensitive[0], declaration_strings[1])
        self.assertEqual(search_results_case_insensitive[1], declaration_strings[3])

    def test_get_declaration(self):
        code_strings = (
            'import hello',
            'from dja import something',
            '#my comment',
            'i+=1',
            'version="1.0.1"',
            '    class Meta:',
            '    def wrapper(func):',
            '    local_var = "something"',
            'my_car.color = "red"',
            'def get_color(car):',
            'class Room(Place):',
            'class Foo:',
            'def stop():',
            'DIR_PATH = my_dir.path()',
        )
        # todo
