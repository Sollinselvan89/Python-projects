from even_odd_sorter import sort_odd_even


def test_mixed_numbers():
    even, odd = sort_odd_even([1, 2, 3, 4])
    assert even == [2, 4]
    assert odd == [1, 3]


def test_all_even():
    even, odd = sort_odd_even([2, 4, 6, 8])
    assert even == [2, 4, 6, 8]
    assert odd == []


def test_all_odd():
    even, odd = sort_odd_even([1, 3, 5])
    assert even == []
    assert odd == [1, 3, 5]


def test_empty_list():
    even, odd = sort_odd_even([])
    assert even == []
    assert odd == []


def test_negative_numbers():
    even, odd = sort_odd_even([-1, -2, -3, -4])
    assert even == [-2, -4]
    assert odd == [-1, -3]
