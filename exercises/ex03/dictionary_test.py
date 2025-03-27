"""EX03 - Dictionary Functions - test"""

__author__: str = "730826007"

import pytest
from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


def test_invert_usecase1() -> None:
    """Test invert with multiple key-value pairs."""
    d = {"A": "Selina", "A*": "July"}
    assert invert(d) == {"Selina": "A", "July": "A*"}


def test_invert_usecase2() -> None:
    """Test invert with single pair."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_edge_case_key_error():
    """Test invert raises KeyError when values are not unique."""
    with pytest.raises(KeyError):
        my_dict = {"kris": "jordan", "michael": "jordan"}
        invert(my_dict)


def test_count_usecase_1():
    """Use case: repeated and unique values mixed."""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_count_usecase_2():
    """Use case: all values are unique."""
    assert count(["cat", "dog", "bird"]) == {"cat": 1, "dog": 1, "bird": 1}


def test_count_edgecase_empty():
    """Edge case: empty list returns empty dictionary."""
    assert count([]) == {}


def test_favorite_color_use_case_1():
    """Use case: clear winner with repeated color."""
    favorites = {"Amy": "red", "Bob": "blue", "Cat": "red"}
    assert favorite_color(favorites) == "red"


def test_favorite_color_use_case_2():
    """Use case: another clear winner."""
    favorites = {"Tom": "green", "Jerry": "green", "Spike": "blue"}
    assert favorite_color(favorites) == "green"


def test_favorite_color_edge_case_tie():
    """Edge case: tie between colors, return first encountered."""
    favorites = {"A": "pink", "B": "blue", "C": "pink", "D": "blue"}
    assert favorite_color(favorites) == "pink"


def test_bin_len_use_case_1():
    """Use case: mix of word lengths."""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_case_2():
    """Use case: repeated words should not duplicate in set."""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge_case_empty():
    """Edge case: empty list should return empty dict."""
    assert bin_len([]) == {}
