import pytest

import solution002 as solution


def test():
    assert solution.sokraschatel("tour") == ".t.r"
    assert solution.sokraschatel("Codeforces") == ".c.d.f.r.c.s"
    assert solution.sokraschatel("aBAcAba") == ".b.c.b"
