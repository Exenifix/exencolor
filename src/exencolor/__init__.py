"""A modern module for colored output. Licensed under MIT (see LICENSE for details)."""
from typing import Any, Sequence

from .enums import *


def colored(
    obj: Any,
    *,
    foreground: Color | int = None,
    background: Color | int = None,
    decoration: Decoration = None,
    decorations: Sequence[Decoration] = None,
) -> str:
    """
    Takes an object and returns its colored string representation.

    :param obj: The object to be colored. Will automatically be converted to str.
    :type obj: Any
    :param foreground: The foreground color of the text. May either be Color enum or a 256 ANSI color code.
    :type foreground: Color | int
    :param background: The background color of the text. May either be Color enum or a 256 ANSI color code.
    :type background: Color | int
    :param decoration: A decoration to apply to text.
    :type decoration: Decoration
    :param decorations: A sequence of decorations to apply to text. If `decoration` is also provided, it is included.
    :type decorations: Sequence[Decoration]
    :return: A colored obj.
    """
    decorations = decorations or []
    if decoration is not None:
        decorations.append(decoration)
    if any(not isinstance(i, Decoration) for i in decorations):
        raise TypeError("Decorations must be of type `Decoration`.")

    obj = str(obj)
    obj = obj.replace("\u001b[0m", "")  # to prevent unexpected reset
    text = ""

    if foreground is not None:
        text += f"\u001b[38;5;{_get_color(foreground)}m"

    if background is not None:
        text += f"\u001b[48;5;{_get_color(background)}m"

    for deco in decorations:
        text += f"\u001b[{deco.value}m"

    return text + obj + "\u001b[0m"


def _get_color(value: Color | int) -> int:
    if not isinstance(value, (Color, int)):
        raise TypeError(
            "Color has to be either `Color` or `int`, not `%s`", type(value)
        )

    return value.value if isinstance(value, Color) else value
