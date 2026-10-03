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

import json
from SublimeLinter.lint import Linter, LintMatch


TAB_STOP = 8


MYPY = False
if MYPY:
    from typing import Iterator


class Hlint(Linter):
    """Provides an interface to hlint."""

    cmd = 'hlint ${args} --json -'
    defaults = {
        'selector': 'source.haskell'
    }

    def find_errors(self, output):
        # type: (str) -> Iterator[LintMatch]
        errors = json.loads(output)

        for error in errors:
            message = "{hint}.\nFound:   {from}".format(**error)
            if error['to']:
                message += "\nPerhaps: {to}".format(**error)
            yield LintMatch(
                error_type=error['severity'].lower(),
                line=error['startLine'] - 1,
                col=error['startColumn'] - 1,
                message=message
            )

    def convert_column(self, line, col, m, vv):
        # GHC source columns count characters, with tabs advancing to the
        # next multiple of `TAB_STOP`. Translate back to a character index.
        text = vv.select_line(line)
        visual = 0
        for index, char in enumerate(text):
            if visual >= col:
                return index
            visual = (visual // TAB_STOP + 1) * TAB_STOP if char == '\t' else visual + 1
        return len(text) + (col - visual)
