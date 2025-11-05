from bill_splitter import *

def test_equal_contributions():
    contribution = {'aa':400, 'bb':400, 'cc':400}
    result = calculate_settlement(contribution)
    expected = {'aa':0, 'bb':0, 'cc':0}
    assert result == expected


def test_one_overpayer():
    contributions = {"aa": 500, "bb": 300, "cc": 400}
    result = calculate_settlement(contributions)
    expected = {"aa": 100.0, "bb": -100.0, "cc": 0.0}
    assert result == expected


def test_single_person():
    contributions = {"aa": 1000}
    result = calculate_settlement(contributions)
    expected = {"aa": 0}
    assert result == expected


def test_display_settlement(capsys):
    data = {"aa": 100, "bb": -100, "cc": 0}
    display_settlement(data)
    captured = capsys.readouterr()
    assert "aa should receive Rs. 100.00" in captured.out
    assert "bb owes Rs.100.00" in captured.out
    assert "cc is settled up." in captured.out