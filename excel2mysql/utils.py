#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals,
                        with_statement, absolute_import)

import os
import re
from excel2mysql.models import TableStructure
from excel2mysql.settings import SQL_FILE_PATH, DEFAULT_CREATE_TABLE_FILE


def validate_file_name(file_name):
    """Validate file name."""
    if not file_name:
        raise TypeError("Invalid filename!")
    if not isinstance(file_name, unicode):
        raise ValueError("Invalid filename!")
    if not os.path.isfile(file_name):
        raise IOError("File not exists: " + file_name)


def read_content(*args):
    """Read file and return content."""
    if len(args) <= 0:
        raise ValueError('Invalid parameter!')
    with open(os.path.join(*args), 'r') as _f:
        return _f.read()


def parse_table_structure(sql_file_path=None):
    """Get all field names from sql creation statement."""
    if sql_file_path is None:
        sql_file_path = os.path.join(SQL_FILE_PATH, DEFAULT_CREATE_TABLE_FILE)
    sql_content = read_content(sql_file_path)
    re_fields = re.compile(r'`\S+`')
    fields = re_fields.findall(sql_content.split('PRIMARY'.encode('utf-8'))[0])

    fields = [each.strip('`') for each in fields]

    return TableStructure(fields[0], fields[1:], None)
