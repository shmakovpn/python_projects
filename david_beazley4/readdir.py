#!/usr/bin/env python
import os
import re
import shutil

project_dir = "/home/shmakovpn/projects/asfo-tile-interface"

ids_names_file = os.path.join(project_dir, 'documents.csv')
doc_names = {}

with open(ids_names_file, 'r') as f:
    for line in f.readlines():
        # print(f"line={line}", end='')
        (id, name, _) = line.split(';', 2)
        try:
            id = int(id.strip('"'))
        except ValueError as e:
            continue
        name = name.strip('"')
        doc_names[id] = name
        # print(f"id={id}; name={name};")

files_source_dir = os.path.join(project_dir, 'files-source')


def find_files(files_source_dir):
    pattern = re.compile(r'^\d+\.pdf$', flags=re.IGNORECASE)
    for path, dirnames, filelist in os.walk(files_source_dir):
        for name in filelist:
            if pattern.match(name):
                yield (path, name)


date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
files_dir = os.path.join(project_dir, 'files')

for path, name in find_files(os.path.join(project_dir, 'files-source')):
    dirname = os.path.basename(path)
    if date_pattern.match(dirname):
        year = dirname[0:4]
        month = dirname[5:7]
        day = dirname[8:10]
        year_dir = os.path.join(files_dir, year)
        if not os.path.isdir(year_dir):
            os.mkdir(year_dir)
            print(f"info: created year_dir={year_dir}")
        month_dir = os.path.join(year_dir, month)
        if not os.path.isdir(month_dir):
            os.mkdir(month_dir)
            print(f"info: created month_dir={month_dir}")
        day_dir = os.path.join(month_dir, day)
        if not os.path.isdir(day_dir):
            os.mkdir(day_dir)
            print(f"info: created day_dir={day_dir}")
        doc_name, _ = name.split(".", 2)
        try:
            doc_name = int(doc_name)
        except ValueError as e:
            continue
        doc_full_name = doc_names[doc_name].replace("/", "-").strip(" .")[:40].strip(" .")
        filename = os.path.join(day_dir, f"{doc_name}_{doc_full_name}.pdf")
        print(f"{filename}")
        if not os.path.isfile(filename):
            shutil.copy2(os.path.join(path, name), filename)
            print(f"copy info: from '{os.path.join(path, name)}' to '{filename}'")
    else:
        print(f"warning: folder not matched to date: {dirname}")
