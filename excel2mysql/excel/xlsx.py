#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals,
                        absolute_import, with_statement)

import logging
import openpyxl


class XlsxFile(object):
    """
    Handle xlsx files and return a matrix of content.
    Usage:
        list_of_tuples = XlsxFile("name.xlsx").matrix
    """
    def __init__(self, excel_file):
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
        self.matrix = []
        self._get_matrix()

    def _get_matrix(self):
        """Get a two dimensional matrix from the xlsx file."""
        for i, row in enumerate(self.ws.rows):
            row_container = []
            for j, cell in enumerate(row):
                row_container.append(cell.value)
            self.matrix.append(tuple(row_container))
