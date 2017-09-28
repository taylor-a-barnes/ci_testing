"""
Tests the ci_testing add functionality
"""

import ci_testing as ct
import pytest

_add_tests = [(4, 3, 7),
              (5.3, 6.7, 12),
              ]

@pytest.mark.parametrize("x,y,result", _add_tests)
def test_add(x, y, result):
    assert result == pytest.approx(ct.add(x,y))
