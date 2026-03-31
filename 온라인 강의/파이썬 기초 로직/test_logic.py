import pytest
from logic_problems import (
    normalize_ws, unique_keep_order, is_valid_brackets, 
    parse_query, merge_sorted
)

def test_normalize_ws():
    assert normalize_ws("  a\t b   c  ") == ("a b c", 3)
    assert normalize_ws("\n\t ") == ("", 0)
    assert normalize_ws("hello world") == ("hello world", 2)

def test_unique_keep_order():
    assert unique_keep_order([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert unique_keep_order([]) == []
    assert unique_keep_order([1, 1, 1]) == [1]

def test_is_valid_brackets():
    assert is_valid_brackets("([]){}") is True
    assert is_valid_brackets("(]") is False
    assert is_valid_brackets("(((") is False
    assert is_valid_brackets("") is True

def test_parse_query():
    assert parse_query("a=1&b=2&b=3") == {"a": ["1"], "b": ["2", "3"]}
    assert parse_query("a=&b=hello") == {"a": [""], "b": ["hello"]}
    assert parse_query("") == {}

def test_merge_sorted():
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted([], [1, 1]) == [1, 1]
    assert merge_sorted([10, 20], [5, 15, 25]) == [5, 10, 15, 20, 25]