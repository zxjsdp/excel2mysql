#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import (print_function, unicode_literals,
                        absolute_import, with_statement)

from excel2mysql.settings import TEMPLATE_MAP
from excel2mysql.settings import IGNORED_FIELDS_FOR_INSERT


def build_drop_sql(table_name):
    """Build drop table SQL statement with table name."""
    return TEMPLATE_MAP.get('DROP_TABLE') % table_name


def filter_ignore_fields(original_fields):
    """Remove fields which are unnecessary for insert statement.
    For example:
        `id`, `created_at`, and `updated_at` will be filtered.
    """
    return [field for field in original_fields
            if field not in IGNORED_FIELDS_FOR_INSERT]


def build_dict_style_insert_sql(table_name, fields):
    """Build insert SQL statement by table name and column names."""
    fields = filter_ignore_fields(fields)

    columns_str = ', '.join(fields)
    values_str = ', '.join(['%%(%s)s' % column for column in fields])

    insert_statement = TEMPLATE_MAP.get('INSERT_INTO') % (table_name,
                                                          columns_str,
                                                          values_str)
    return insert_statement
