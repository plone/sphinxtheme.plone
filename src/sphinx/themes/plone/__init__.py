#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from sphinx.errors import ThemeError



def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return cur_dir
    
def get_html_theme_subpath():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    theme_dirs = [] 
    for item in os.listdir(cur_dir):
        cur_file = os.path.join(cur_dir, item)
        if os.path.isdir(os.path.abspath(cur_file)):
            theme_dirs.append(os.path.abspath(cur_file))

    return theme_dirs

def get_html_theme_path_for_theme(theme='plone_org_4'):
    theme_dirs = []
    cur_dir = os.path.abspath(os.path.dirname(__file__))

    # lookup base folders for themes
    static_dir = os.path.join(cur_dir,'static')
    if os.path.exists(static_dir) and os.path.isdir(static_dir):
        theme_dirs.append(static_dir)
    template_dir = os.path.join(cur_dir,'templates')
    if os.path.exists(template_dir) and os.path.isdir(template_dir):
        theme_dirs.append(template_dir)
    basetheme_dir = os.path.join(cur_dir,'plone_basic')
    if os.path.exists(basetheme_dir) and os.path.isdir(basetheme_dir):
        theme_dirs.append(basetheme_dir)

    # lookup theme
    theme_dir = os.path.join(cur_dir,theme)
    if os.path.exists(theme_dir) and os.path.isdir(theme_dir):
        theme_dirs.append(theme_dir)
    else:
        raise ThemeError('Theme not found')
    return theme_dirs

if __name__ == '__main__':
    print get_html_theme_path()
    print get_html_theme_path_for_theme()

