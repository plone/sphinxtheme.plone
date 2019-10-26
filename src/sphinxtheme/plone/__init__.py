#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    return [cur_dir]


if __name__ == '__main__':
    print(get_html_theme_path())
