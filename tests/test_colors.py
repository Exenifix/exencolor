from exencolor import Decoration, colored, Color


def print_and_assert(obj, expected):
    print(obj)
    assert obj == expected


def test_foregrounds():
    print()
    assertion_cases = (
        ("blue text", Color.BLUE, "\x1b[38;5;4mblue text\x1b[0m"),
        ("green text", Color.GREEN, "\x1b[38;5;2mgreen text\x1b[0m"),
        ("bright yellow text", Color.BRIGHT_YELLOW, "\x1b[38;5;11mbright yellow text\x1b[0m")
    )
    for case, color, result in assertion_cases:
        print_and_assert(colored(case, color), result)


def test_backgrounds():
    print()
    assertion_cases = (
        ("cyan background", Color.CYAN, "\x1b[48;5;6mcyan background\x1b[0m"),
        ("red background", Color.RED, "\x1b[48;5;1mred background\x1b[0m"),
        ("bright magenta", Color.BRIGHT_MAGENTA, "\x1b[48;5;13mbright magenta\x1b[0m")
    )
    for case, color, result in assertion_cases:
        print_and_assert(colored(case, background=color), result)


def test_decorations():
    print()
    assertion_cases = (
        ("underlined", Decoration.UNDERLINE, "\x1b[4munderlined\x1b[0m"),
        ("bold", Decoration.BOLD, "\x1b[1mbold\x1b[0m")
    )
    for case, deco, result in assertion_cases:
        print_and_assert(colored(case, decoration=deco), result)
