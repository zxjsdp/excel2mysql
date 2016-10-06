# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals,
                        absolute_import, with_statement)

import os

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MySQL connection config
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_AUTH = ''
MYSQL_DATABASE = 'playground'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SQL path & names
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SQL_FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'sqls')
DEFAULT_CREATE_TABLE_FILE = 'create.sql'
IGNORED_FIELDS_FOR_INSERT = ['id', 'created_at', 'updated_at']


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SQL templates
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TEMPLATE_MAP = {
    'SHOW_TABLES': """SHOW TABLES""",
    'DROP_TABLE': """DROP TABLE %s""",
    'SELECT_HEAD': """SELECT * FROM %s LIMIT 10""",
    'INSERT_INTO': """INSERT INTO %s (%s) VALUES (%s)""",
}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Charset
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MYSQL_CHAR_SET = 'utf8'

CHAR_RELATED_STATEMENTS = [
    "cursor.execute('SET NAMES utf8;')",
    "cursor.execute('SET CHARACTER SET utf8;')",
    "cursor.execute('SET character_set_connection=utf8;')'"
]
