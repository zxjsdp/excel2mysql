#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals,
                        absolute_import, with_statement)

import os
import MySQLdb
import openpyxl
import logging

from excel2mysql.settings import DEFAULT_CREATE_TABLE_FILE
from excel2mysql.settings import MYSQL_AUTH
from excel2mysql.settings import MYSQL_CHAR_SET
from excel2mysql.settings import MYSQL_DATABASE
from excel2mysql.settings import MYSQL_HOST
from excel2mysql.settings import MYSQL_PORT
from excel2mysql.settings import MYSQL_USER
from excel2mysql.settings import SQL_FILE_PATH
from excel2mysql.settings import TEMPLATE_MAP
from excel2mysql.settings import HAS_HERDER_ROW
from excel2mysql.mysql import filter_ignore_fields


class MySQLClient(object):
    """Client for commonly used MySQL operations."""
    def __init__(self):
        self.conn = None
        self.cur = None
        self._prepare_conn()

    def _prepare_conn(self):
        try:
            self.conn = MySQLdb.Connection(
                host=MYSQL_HOST,
                port=MYSQL_PORT,
                user=MYSQL_USER,
                passwd=MYSQL_AUTH,
                db=MYSQL_DATABASE
            )
            self.cur = self.conn.cursor()
            self.conn.set_character_set(MYSQL_CHAR_SET)
        except TypeError as e:
            raise
        except MySQLdb.ProgrammingError as e:
            raise
        except Exception as e:
            raise

    def query(self, query=None):
        """Query with given SQL statement."""
        if not query:
            raise SyntaxWarning("No SQL query statement!")
        else:
            self.conn.query(query)
            result = self.conn.store_result()
            for i in range(result.num_rows()):
                yield result.fetch_row()

    def query_all(self, query=None):
        """Query with given SQL statement."""
        if not query:
            raise SyntaxWarning("No SQL query statement!")
        else:
            self.cur.execute(query)
            return self.cur.fetchall()

    def execute(self, statement=None):
        """Execute SQL statement, create table, insert, ..."""
        if not statement:
            raise SyntaxWarning("No valid SQL statement!")
        else:
            try:
                self.cur.execute(statement)
                self.conn.commit()
                return self.conn.affected_rows()
            except Exception as e:
                self.conn.rollback()
                raise

    def execute_many_by_list(self, statement, data_list):
        """Execute SQL statement, create table, insert, ..."""
        if not statement or len(data_list) <= 0:
            raise SyntaxWarning("No valid SQL statement!")
        elif not isinstance(data_list, list):
            raise TypeError(
                "Parameter data_list must be list type "
                "which contains row data!")
        else:
            try:
                self.cur.executemany(statement, data_list)
                self.conn.commit()
                return self.conn.affected_rows()
            except Exception as e:
                self.conn.rollback()
                raise

    def execute_many_by_dict(self, statement, data_dict):
        """Execute SQL statement, create table, insert, ..."""
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
        print(statement)
        print(data_dict)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
        if not statement or len(data_dict) <= 0:
            raise SyntaxWarning("No valid SQL statement!")
        elif not isinstance(data_dict[0], dict):
            raise TypeError(
                "Parameter data_dict must be dict type "
                "which contains row data!")
        else:
            try:
                self.cur.executemany(statement, data_dict)
                self.conn.commit()
                return self.conn.affected_rows()
            except Exception as e:
                self.conn.rollback()
                raise

    def create_table(self, force=False):
        """Create new MySQL table. Drop if it already exists."""
        from excel2mysql.utils import parse_table_structure
        from excel2mysql.utils import read_content
        sql_file_path = os.path.join(
            SQL_FILE_PATH, DEFAULT_CREATE_TABLE_FILE)
        table_name = parse_table_structure(sql_file_path).table_name
        if table_name in self.show_tables() and force:
            self.drop_table(table_name)
        self.execute(read_content(
            SQL_FILE_PATH, DEFAULT_CREATE_TABLE_FILE))

    def show_tables(self):
        """List all tables in current database."""
        table_names = []
        for each in self.query(TEMPLATE_MAP.get('SHOW_TABLES')):
            table_names.append(each[0][0])
        return table_names

    def drop_table(self, table_name):
        """Drop table."""
        self.execute(TEMPLATE_MAP.get('DROP_TABLE') % table_name)

    def __del__(self):
        """Close db connection finally."""
        self.conn.close()


class TableStructure(object):
    """MySQL table name, fields (list of columns), and indexes"""
    def __init__(self, table_name, fields, indexes):
        self.table_name = table_name
        self.fields = fields
        self.indexes = indexes


class XlsxFile(object):
    """
    Handle xlsx files and return a matrix of content.
    Usage:
        list_of_tuples = XlsxFile("name.xlsx", ('id', 'name', 'age')).matrix
    """
    def __init__(self, excel_file, field_names):
        try:
            self.wb = openpyxl.load_workbook(excel_file)
        # Invalid xlsx format
        except openpyxl.utils.exceptions.InvalidFileException as e:
            logging.error("Invalid xlsx format.\n%s" % e)
            raise
        except IOError as e:
            logging.error("No such xlsx file: %s. (%s)" % (excel_file, e))
            raise
        except BaseException as e:
            logging.error('Unknown error. (%s)' % e)
            raise

        self.ws = self.wb.active
        self.ws_title = self.ws.title
        self.field_names = field_names
        self.matrix = []
        self._get_matrix()

    @property
    def data_dict_list(self):
        list_of_dict = []
        fields_for_insert = filter_ignore_fields(self.field_names)
        for index, row in enumerate(self.matrix):
            info_dict = {}
            if len(fields_for_insert) != len(row):
                raise ValueError(
                    "Size of Excel row does not match SQL field names. "
                    "(index: %d; row: %s; fields: %s)" %
                    (index, row, fields_for_insert))
            for field_index, field in enumerate(fields_for_insert):
                info_dict[field] = row[field_index]
            list_of_dict.append(info_dict)

        return list_of_dict

    def _get_matrix(self):
        """Get a two dimensional matrix from the xlsx file."""
        for i, row in enumerate(self.ws.rows):
            row_container = []
            for j, cell in enumerate(row):
                row_container.append(cell.value)
            self.matrix.append(tuple(row_container))

        if HAS_HERDER_ROW:
            self.matrix.pop(0)
