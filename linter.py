#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Hardy Jones
# Copyright (c) 2013
#
# License: MIT
#

"""This module exports the Hlint plugin class."""

from SublimeLinter.lint import Linter


class Hlint(Linter):
    """Provides an interface to hlint."""

    syntax = ('haskell', 'haskell-sublimehaskell', 'literate haskell')
    cmd = 'hlint'
    regex = (
        r'^.+:(?P<line>\d+):'
        '(?P<col>\d+):\s*'
        '(?:(?P<error>Error)|(?P<warning>Warning)):\s*'
        '(?P<message>.+)$'
    )
    multiline = True
    tempfile_suffix = {
        'haskell': 'hs',
        'haskell-sublimehaskell': 'hs',
        'literate haskell': 'lhs'
    }
