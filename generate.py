#!/usr/bin/env python3

import datetime
import os
import sys

import jinja2

def date_format(value, strformat="%Y-%m-%d"):
    return value.strftime(strformat)

global_vars = {}

for arg in sys.argv[1:]:
    key, _, value = arg.partition('=')
    global_vars[key] = value

env = jinja2.Environment(keep_trailing_newline=True, loader=jinja2.FileSystemLoader(os.getcwd() + '/templates'))

env.globals = global_vars
env.filters['date_format'] = date_format

version_dirs = [item.name for item in os.scandir() if item.is_dir() and 'OpenWrt' in item.name]
versions = [item.partition('_')[2] for item in version_dirs]
versions_and_dirs = sorted(zip(versions, version_dirs), reverse=True)

template = env.get_template('toplevel-readme.jinja')
stream = template.stream(versions_and_dirs=versions_and_dirs)
stream.dump(open('README.md', 'w'))

for version, version_dir in versions_and_dirs:
    os.chdir(version_dir)

    arches = sorted([item.name for item in os.scandir() if item.is_dir()])

    template = env.get_template('version-readme.jinja')
    stream = template.stream(version=version, arches=arches)
    stream.dump(open('README.md', 'w'))

    for arch in arches:
        os.chdir(arch)

        context = {
                'version': version,
                'version_dir': version_dir,
                'arch': arch,
                'date': datetime.date.today(),
        }
        template = env.get_template('arch-readme.jinja')
        stream = template.stream(context)
        stream.dump(open('README.md', 'w'))

        os.chdir('..')

    os.chdir('..')
