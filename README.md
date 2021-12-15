SublimeLinter-hlint
=========================

[![flake8](https://github.com/SublimeLinter/SublimeLinter-hlint/actions/workflows/flake8.yml/badge.svg)](https://github.com/SublimeLinter/SublimeLinter-hlint/actions/workflows/flake8.yml)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [hlint](http://community.haskell.org/~ndm/hlint/).
It will be used with files that have the "Haskell" syntax.


## Installation

SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, ensure that `hlint` is installed on your system.
To install `hlint`, do the following:

1. Ensure [cabal](http://www.haskell.org/cabal/) is installed. The easiest way is to install the [haskell platform](http://www.haskell.org/haskellwiki/Haskell), as this gives you cabal also. 

2. Update cabal:
    ```
    cabal update
    ```
3. Install `hlint` with cabal:
    ```
    cabal install hlint
    ```

Please make sure that the path to `hlint` is available to SublimeLinter.
The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html
