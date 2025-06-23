from shaksz import leetcode
import pytest


def test_lc_twoSum():
    result = leetcode.twoSum([2, 7, 11, 15], 9)
    assert result == [0, 1]

def test_lc_threeConsecutiveOdds():
    result = leetcode.threeConsecutiveOdds([2, 6, 4, 1])
    assert result is False