from debug import broken_loop, broken_nested

TEST_SUITE_NAME = "Debug Tests"


def test_broken_loop():
    """broken_loop - builds a string from start (inclusive) to end (inclusive) by 1"""
    assert broken_loop(1, 10) == "12345678910"
    assert broken_loop(5, 12) == "56789101112"
    assert broken_loop(0, 0) == "0"
    assert broken_loop(0, -1) == ""


def test_broken_nested():
    """broken_nested - builds a string of numbers from 00 to 19"""
    expected = "00-01-02-03-04-05-06-07-08-09-10-11-12-13-14-15-16-17-18-19"
    assert broken_nested() == expected
