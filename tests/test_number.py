from stedders import number


def test_initial_number():
    assert number == 1


def test_addition():
    assert number + 5 == 6


def test_multiplcation():
    assert number * 5 == 5


def test_subtraction():
    assert number - 5 == -4
