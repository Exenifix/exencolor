from enum import Enum


class Color(Enum):
    """
    An enum containing some color codes.
    """

    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7
    GREY = 8
    BRIGHT_RED = 9
    BRIGHT_GREEN = 10
    BRIGHT_YELLOW = 11
    BRIGHT_BLUE = 12
    BRIGHT_MAGENTA = 13
    BRIGHT_CYAN = 14
    BRIGHT_WHITE = 15


class Decoration(Enum):
    """
    An enum containing some decoration codes.
    """

    BOLD = 1
    UNDERLINE = 4
    REVERSED = 7
