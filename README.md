# EOL Ender
Fix line endings recursively in all the files in the current directory with a single command!

# What does this do exactly?
This script changes the EOL characters in all files (optionally with a specified extention) to `LF`.
It doesn't touch `.ps`, `.bat`, `.cmd` or `.btm` files as they are DOS specific files and should have `CRLF` line endings.

# Requirements

* [Python 3](https://www.python.org/downloads/)
* [EOL Ender Script](https://raw.github.com/k3rn31p4nic/eol-ender/master/ender.py)

# Usage

```
ender.py [DIRECTORY] [EXTENSION]
```

## Arguments

* `DIRECTORY`  
  The path (relative or absolute) to the directory in which the files are to be searched. Defaults to the current working directory `.`.
* `EXTENSION`  
  If the extension is specified, only the files with this extension will be changed. Defaults to all the files in the current and sub directories.

## Examples

1. Fix line endings for all files inside the current directory (and subdirectories).
```
ender.py
```

2. Fix line endings for all files inside the `parser` directory (and its subdirectories).
```
ender.py parser
```

3. Fix line endings for all files, with `.go` extention, inside the current directory (and subdirectories).
```
ender.py . go
```

4. Fix line endings for all files, with `.prism` extention, inside the `examples` directory (and its subdirectories).
```
ender.py examples prism
```

# Notes

> To download this script, [Right-Click here](https://raw.github.com/k3rn31p4nic/eol-ender/master/ender.py) and click **Save Link As...** and save the file.

> Feel free to open issues and/or pull requests if you want to contribute.
