#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals,
                        absolute_import, with_statement)

from excel2mysql.models import XlsxFile
from excel2mysql.utils import parse_table_structure
from excel2mysql.utils import validate_file_name


def get_all_as_list(excel_file):
    """Get data from Excel file."""
    validate_file_name(excel_file)
    lines_of_tuples = XlsxFile(excel_file).matrix

    return lines_of_tuples


def get_all_as_dict(excel_file):
    """Migrate data from Excel file to MySQL."""
    validate_file_name(excel_file)
    field_names = parse_table_structure().fields
    data_dict_list = XlsxFile(excel_file, field_names).data_dict_list

    return data_dict_list
