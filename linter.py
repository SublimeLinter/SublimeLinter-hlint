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
            message = "{hint}. Found: {from}".format(**error)
            if error['to']:
                message += " Perhaps: {to}".format(**error)
            yield LintMatch(
                error_type=error['severity'].lower(),
                line=error['startLine'] - 1,
                col=error['startColumn'] - 1,
                message=message
            )
