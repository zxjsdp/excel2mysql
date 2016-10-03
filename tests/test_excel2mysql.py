#!/usr/bin/env python
# -*- coding: utf-8 -*-

from excel2mysql import excel2mysql

test_xlsx_file = 'test.xlsx'


def test_extract_all_excel_data():
    out = excel2mysql.extract_all_excel_data(test_xlsx_file)
    assert len(out) == 11
    assert len(out[0]) == 5
