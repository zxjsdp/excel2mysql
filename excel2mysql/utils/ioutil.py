#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals,
                        with_statement, absolute_import)

import os


def validate_file_name(file_name):
    """Validate file name."""
    if not file_name:
        raise TypeError("Invalid filename!")
    if not isinstance(file_name, str):
        raise ValueError("Invalid filename!")
    if not os.path.isfile(file_name):
        raise IOError("File not exists: " + file_name)
