from character_counter import count_character

def test_count_charcter(): #pytest
    text = "Hello! My name is Johnnathan"
    chars,words = count_character(text)
    assert chars == 28
    assert words == 5
    