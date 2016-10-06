#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Export data from Excel file to MySQL database."""

from __future__ import (print_function, unicode_literals,
                        absolute_import, with_statement)

import os

from excel2mysql.models import MySQLClient
from excel2mysql.mysql import build_dict_style_insert_sql
from excel2mysql.utils import parse_table_structure
from excel2mysql.excel import get_all_as_dict


def migrate():
    client = MySQLClient()
    table_structure = parse_table_structure()
    data_dict = get_all_as_dict(
        os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__))),
            'tests',
            'test.xlsx'
        )
    )
    client.execute_many_by_dict(
        build_dict_style_insert_sql(
            table_name=table_structure.table_name,
            fields=table_structure.fields),
        data_dict)


def main():
    pass

if __name__ == '__main__':
    main()
