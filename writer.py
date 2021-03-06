#!/usr/bin/python
# -*- coding: utf8 -*-
"""Module for simple writing operations."""
import codecs
import json
import filepath


def write(path, content, encoding='utf-8'):
    """Write the content to a file."""
    filepath.create_path(path)
    with codecs.open(path, 'w', encoding) as f:
        f.write(content)


def write_json(path, content, encoding='utf-8', indent=2):
    """Write the json to a file."""
    filepath.create_path(path)
    str_content = json.dumps(content, indent=indent)
    write(path, str_content, encoding)
