#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals,
                        absolute_import, with_statement)

from excel2mysql import migrate

test_xlsx_file = 'test.xlsx'


def test_migration():
    migrate.migrate()
