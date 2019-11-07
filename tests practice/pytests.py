import pytest

from functions import (convert_number_to_hours,
                       largest_word,
                       words_in_backwards_order,
                       fibonacci,
                       even_nums,
                       add_up_numbers,
                       factorial,
                       replace_letters_in_str,
                       sorted_word,
                       number_compare)


def test_convert_number_to_hours():
    assert convert_number_to_hours(63) == '1 : 3'


def test_largest_word():
    assert largest_word('fun&!! time') == 'time'
    assert largest_word('I love dogs') == 'love'
    assert largest_word('I d_!& dogs') == 'dogs'
    assert largest_word('Very interesting text') == 'interesting'


def test_words_in_backwards_order(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: 'My name is Michele')
    assert words_in_backwards_order('My name is Michele') == 'Michele is name My'


def test_fibonacci():
    assert fibonacci(7) == [1, 1, 2, 3, 5, 8, 13]


def test_even_nums():
    assert even_nums([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == [4, 16, 36, 64, 100]


def test_add_up_numbers():
    assert add_up_numbers(4) == 10


def test_factorial():
    assert factorial(4) == 24


def test_replace_letters_in_str():
    assert replace_letters_in_str('abcd') == 'bcdE'


def test_sorted_word():
    assert sorted_word('edcba') == 'abcde'


def test_number_compare():
    assert number_compare(1, 2) is True
    assert number_compare(1, 1.0) == '-1'
    assert number_compare(2, 1) is False
