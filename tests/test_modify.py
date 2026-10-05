import inspect

from modify import continue_guard_clause, while_to_for

TEST_SUITE_NAME = "Modify Tests"


def body_of(func):
    """The function's source WITHOUT its `def` line.

    Python's inspect.getsource includes the signature, so checking the whole
    source for "while" would always match `def while_to_for`, and checking
    for "continue" would always match `def continue_guard_clause`.
    """
    lines = inspect.getsource(func).splitlines()
    start = next(i for i, line in enumerate(lines) if line.rstrip().endswith(":"))
    return "\n".join(lines[start + 1:])


def printed(capsys):
    return [line for line in capsys.readouterr().out.splitlines() if line.strip()]


def test_while_to_for_no_longer_uses_while():
    """while_to_for - no longer uses a while loop"""
    body = body_of(while_to_for)
    assert "while" not in body
    assert "for" in body


def test_while_to_for_output(capsys):
    """while_to_for - it prints from 0 (inclusive) to 5 (exclusive) by 1"""
    body = body_of(while_to_for)  # repeated to avoid an automatic pass
    assert "while" not in body
    assert "for" in body

    while_to_for()
    assert printed(capsys) == ["0", "1", "2", "3", "4"]


def test_continue_guard_clause_uses_continue():
    """continue_guard_clause - uses a continue statement"""
    assert "continue" in body_of(continue_guard_clause)


def test_continue_guard_clause_output(capsys):
    """continue_guard_clause - it prints 1 to 5 (exclusive), skipping 2 and 3"""
    assert "continue" in body_of(continue_guard_clause)

    continue_guard_clause()
    assert printed(capsys) == [
        "Sure glad this isn\'t 2 or 3",
        "1",
        "Sure glad this isn\'t 2 or 3",
        "4",
    ]
