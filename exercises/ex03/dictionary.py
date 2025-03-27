"""EX03 - Dictionary Functions"""

__author__: str = "730826007"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Invert dict; KeyError if duplicate values."""
    result: dict[str, str] = {}
    for key in d:
        value = d[key]
        if value in result:
            raise KeyError(f"Duplicate key in inverted dictionary: {value}")
        result[value] = key
    return result


def count(values: list[str]) -> dict[str, int]:
    """Return a dictionary with counts of each unique string in the list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(favorites: dict[str, str]) -> str:
    """Return most common color; if tie, return first color seen."""
    color_count: dict[str, int] = {}

    for color in favorites.values():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    max_count = 0
    most_frequent = ""
    for color in favorites.values():
        if color_count[color] > max_count:
            max_count = color_count[color]
            most_frequent = color

    return most_frequent


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Group strings by their length into sets."""
    result: dict[int, set[str]] = {}

    for word in words:
        length = len(word)
        if length in result:
            result[length].add(word)
        else:
            result[length] = {word}

    return result
