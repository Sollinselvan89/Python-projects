import string
from password_generator import generate_password  


def test_password_length():
    """Password should match the requested length."""
    choices = {
        "upper_case": "y",
        "lower_case": "y",
        "digits": "y",
        "punctuations": "y",
    }

    pwd = generate_password(12, choices)
    assert len(pwd) == 12


def test_password_allowed_characters():
    """Password should contain only characters from allowed pool."""
    choices = {
        "upper_case": "y",
        "lower_case": "n",
        "digits": "y",
        "punctuations": "n",
    }

    allowed = string.ascii_uppercase + string.digits
    pwd = generate_password(20, choices)

    for char in pwd:
        assert char in allowed


def test_password_randomness():
    """Two generated passwords should rarely look identical."""
    choices = {
        "upper_case": "y",
        "lower_case": "y",
        "digits": "y",
        "punctuations": "y",
    }

    pwd1 = generate_password(15, choices)
    pwd2 = generate_password(15, choices)

    assert pwd1 != pwd2   # Very unlikely to be equal
