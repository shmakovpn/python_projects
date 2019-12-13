#!/usr/bin/env python
"""
This script is an example
"""
import os
import re
from datetime import datetime
from docx import Document
from docx.opc.exceptions import PackageNotFoundError

# current script path
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
print(f"SCRIPT_PATH={SCRIPT_PATH}")

# current datetime
today_str = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
datetime_begin = datetime.now()


def docx_replace(doc_obj, search_str, replace_str, count=-1):
    """
    This function replaces 'search' text in docx document 'doc_obj' to 'replace' text
    :param doc_obj: docx document handler
    :param search_str: the text to search
    :param replace_str: the text to replace
    :param count: integer, Maximum number of occurrences to replace, -1 (the default value) means replace all
        occurrences
    :return: None
    """
    for p in doc_obj.paragraphs:
        if search_str in p.text:
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                if search_str in inline[i].text:
                    text = inline[i].text.replace(search_str, replace_str, count)
                    inline[i].text = text
    for table in doc_obj.tables:
        for row in table.rows:
            for cell in row.cells:
                docx_replace(cell, search_str, replace_str, count)


def docx_replace_context(doc_obj, context, count=-1):
    """
    This function replaces all keys of context dict to its values
    :param doc_obj: docx document handler
    :param context: dict of keys to search and values to replace
    :param count: count: integer, Maximum number of occurrences to replace, -1 (the default value) means replace all
        occurrences
    :return: None
    """
    for key in context:
        docx_replace(doc_obj, key, context[key], count)


# prepare context
context = {
    '{date}': today_str,
    '{username}': 'Шмаков Павел Николаевич',
    '{tag1}': 'тэг1',
    '{list0.element0}': 'первый пункт',
    'list0.element2}': 'целиком пункт два',
    '{table0[0,0]}': 'заголовок 1',
    '{table0[0,1]}': 'заголовок 2',
    '{table0[0,2]}': 'заголовок 3',
    '{table0[1,0]}': 'ячейка 1',
    '{table0[1,1]}': 'ячейка 2',
    '{table0[1,2]}': 'ячейка 3',
}

# open docx document
in_docx_filename = os.path.join(SCRIPT_PATH, "search_replace_example.docx")
out_docx_filename = os.path.join(SCRIPT_PATH, "result.docx")
doc = Document(in_docx_filename)
docx_replace_context(doc, context)
doc.save(out_docx_filename)
print(f"END")


from datetime import timedelta
from datetime import datetime
dt = datetime.now()
