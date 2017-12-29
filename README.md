SublimeLinter-hlint
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-hlint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-hlint)

This linter plugin for [SublimeLinter][SublimeLinter] provides an interface to [hlint][hlint]. It will be used with files that have the “Haskell” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, you must ensure that `hlint` is installed on your system. To install `hlint`, do the following:

1. Ensure [cabal][cabal] is installed. The easiest way is to install the [haskell platform][haskell platform], as this gives you [cabal][cabal] also. If you'd like to install with some other method, these resources will help: [haskell][haskell], [cabal][cabal]
1. Update cabal:
    ```
    cabal update
    ```
1. Install `hlint` with cabal:
    ```
    cabal install hlint
    ```

In order for `hlint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html


[SublimeLinter]: http://sublimelinter.readthedocs.org
[hlint]: http://community.haskell.org/~ndm/hlint/
[haskell platform]: http://www.haskell.org/platform/
[haskell]: http://www.haskell.org/haskellwiki/Haskell
[cabal]: http://www.haskell.org/cabal/
