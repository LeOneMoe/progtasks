import pytest

import solution003 as solution


def test():
    assert solution.is_balanced("a + (13 / 34)) + 8 * [1, 2, 3] ** (34 / 5)") == False
    assert solution.is_balanced("a = map(lambda x: , filter(lambda u: u % 34 == 0 , [y.strip().lower() for y in [t ** 3 for t in range(15)]]))") == True
    assert solution.is_balanced("\"a + (18 / 3) + [ } * []\"") == False
