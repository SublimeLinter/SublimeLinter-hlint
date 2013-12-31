SublimeLinter-hlint
=========================

This linter plugin for [SublimeLinter][SublimeLinter] provides an interface to [hlint][hlint]. It will be used with files that have the “Haskell” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][SublimeLinter Installation].

### Linter installation
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

Once hlint is installed, you can proceed to install the SublimeLinter-hlint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][Package Control] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][Command Palette] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `hlint`. Among the entries you should see `SublimeLinter-hlint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][SublimeLinter Settings]. For information on generic linter settings, please see [Linter Settings][SublimeLinter Linter Settings].

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbrevations unless they are very well known.

Thank you for helping out!

[SublimeLinter]: https://github.com/SublimeLinter/SublimeLinter3
[SublimeLinter Installation]: https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Installation
[SublimeLinter Settings]: https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Settings
[SublimeLinter Linter Settings]: https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Linter-Settings
[Package Control]: https://sublime.wbond.net/installation
[Command Palette]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[hlint]: http://community.haskell.org/~ndm/hlint/
[haskell platform]: http://www.haskell.org/platform/
[haskell]: http://www.haskell.org/haskellwiki/Haskell
[cabal]: http://www.haskell.org/cabal/
