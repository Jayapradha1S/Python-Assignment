from src.email17.util import fun, filter_emails


def test_valid_email():
    assert fun("lara@hackerrank.com") is True


def test_valid_email_with_dash():
    assert fun("brian-23@hackerrank.com") is True


def test_valid_email_with_underscore():
    assert fun("britts_54@hackerrank.com") is True


def test_invalid_extension():
    assert fun("abc@test.comm") is False


def test_invalid_username():
    assert fun("abc!@test.com") is False


def test_invalid_website():
    assert fun("abc@test#.com") is False


def test_filter_emails():
    emails = [
        "abc@test.com",
        "abc!@test.com",
        "john_1@test.org",
        "xyz@test.comm"
    ]

    expected = [
        "abc@test.com",
        "john_1@test.org"
    ]

    assert filter_emails(emails) == expected