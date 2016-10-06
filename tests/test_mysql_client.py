#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals,
                        with_statement, absolute_import)

from excel2mysql.mysql import build_dict_style_insert_sql


def test_build_dict_style_insert_sql():
    table_name = 'table_name'
    fields = ['id', 'name', 'age', 'created_at', 'updated_at']

    expected_sql_statement = ('INSERT INTO table_name (name, age) '
                              'VALUES (%(name)s, %(age)s)')
    actual_sql_statement = build_dict_style_insert_sql(
        table_name, fields)

    assert expected_sql_statement == actual_sql_statement
