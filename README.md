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
![output](.github/img/foreground.png)

### Background

```python
from exencolor import colored, Color

print(colored("Hello World!", background=Color.BLUE))
```
![output](.github/img/background.png)

### Decorations

```python
from exencolor import colored, Decoration

print(colored("Hello World!", decoration=Decoration.UNDERLINE))
```
![output](.github/img/deco1.png)

```python
from exencolor import colored, Decoration

print(colored("Hello World!", decorations=[Decoration.UNDERLINE, Decoration.BOLD]))
```
![output](.github/img/deco2.png)

### Combined

```python
from exencolor import colored, Decoration, Color

print(colored("Hello World!", foreground=Color.BRIGHT_CYAN, background=Color.BRIGHT_YELLOW, decoration=Decoration.UNDERLINE))
```
![output](.github/img/combined.png)
