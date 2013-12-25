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

from SublimeLinter.lint import Linter, util


class Hlint(Linter):

    """Provides an interface to hlint."""

    syntax = ('haskell', 'literate haskell', 'haskell-sublimehaskell')
    cmd = 'hlint'
    regex = r'''(?xi)
        ^.+:(?P<line>\d+):\d+:\s*(?:(?P<error>Error)|(?P<warning>Warning)):\s*(?P<message>.+)$\r?\n
        ^.+$\r?\n
        ^\s*(?P<near>.+)$\r?\n
    '''
    multiline = True
    tempfile_suffix = 'hs'
    error_stream = util.STREAM_BOTH
