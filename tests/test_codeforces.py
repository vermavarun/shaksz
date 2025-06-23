from shaksz import codeforces
import pytest

def test_cf_4a():
    # Test case 1: Even number greater than 2
    input_data = "4"
    expected_output = "Yes"
    assert codeforces._4a(input_data) == expected_output

    # Test case 2: Odd number
    input_data = "3"
    expected_output = "No"
    assert codeforces._4a(input_data) == expected_output

    # Test case 3: Even number equal to 2
    input_data = "2"
    expected_output = "No"
    assert codeforces._4a(input_data) == expected_output

    # Test case 4: Large even number
    input_data = "1000000"
    expected_output = "Yes"
    assert codeforces._4a(input_data) == expected_output