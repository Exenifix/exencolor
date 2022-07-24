![tests](https://github.com/Exenifix/exencolor/actions/workflows/test.yml/badge.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/exencolor)
![License](https://img.shields.io/github/license/Exenifix/exencolor)
![PyPI - Version](https://img.shields.io/pypi/v/exencolor)
![CodeFactor](https://www.codefactor.io/repository/github/exenifix/exencolor/badge)

# ExenColor
A modern module for colored output.


## Installation
The module is available for installation from PyPI via pip:
```shell
$ pip install exencolor
```

## Examples

### Foreground

```python
from exencolor import colored, Color

print(colored("Hello World!", foreground=Color.GREEN))
```
![output](https://github.com/Exenifix/exencolor/blob/master/.github/img/foreground.png?raw=true)

### Background

```python
from exencolor import colored, Color

print(colored("Hello World!", background=Color.BLUE))
```
![output](https://github.com/Exenifix/exencolor/blob/master/.github/img/background.png?raw=true)

### Decorations

```python
from exencolor import colored, Decoration

print(colored("Hello World!", decoration=Decoration.UNDERLINE))
```
![output](https://github.com/Exenifix/exencolor/blob/master/.github/img/deco1.png?raw=true)

```python
from exencolor import colored, Decoration

print(colored("Hello World!", decorations=[Decoration.UNDERLINE, Decoration.BOLD]))
```
![output](https://github.com/Exenifix/exencolor/blob/master/.github/img/deco2.png?raw=true)

### Combined

```python
from exencolor import colored, Decoration, Color

print(colored("Hello World!", foreground=Color.BRIGHT_CYAN, background=Color.BRIGHT_YELLOW, decoration=Decoration.UNDERLINE))
```
![output](https://github.com/Exenifix/exencolor/blob/master/.github/img/combined.png?raw=true)
