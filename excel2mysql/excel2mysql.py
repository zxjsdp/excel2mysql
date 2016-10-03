#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Export data from Excel file to MySQL database."""

from .excel import XlsxFile
from .utils import validate_file_name


def extract_all_excel_data(excel_file):
    """Get data from Excel file."""
    validate_file_name(excel_file)
    lines_of_tuples = XlsxFile(excel_file).matrix

    return lines_of_tuples


def main():
    pass

if __name__ == '__main__':
    main()
