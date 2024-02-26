"""Test module for very big sum."""

import pytest
from a_very_big_sum.a_very_big_sum import a_very_big_sum

def test_empty_list():
    """Test an empty list."""
    assert a_very_big_sum([]) == 0

def test_single_element():
    """Test a single element."""
    assert a_very_big_sum([5]) == 5

def test_positive_numbers():
    """Test all positive numbers."""
    assert a_very_big_sum([1, 2, 3, 4, 5]) == 15

def test_negative_numbers():
    """Test all negative numbers."""
    assert a_very_big_sum([-1, -2, -3, -4, -5]) == -15

def test_mixed_numbers():
    """Test mixed numbers."""
    assert a_very_big_sum([-1, 2, -3, 4, -5]) == -3

def test_large_numbers():
    """Test large numbers."""
    assert a_very_big_sum([10**6, 10**6, 10**6]) == 3 * 10**6

def test_mixed_types():
    """Test proper exception handling."""
    with pytest.raises(TypeError):
        a_very_big_sum([1, 2, '3'])

if __name__ == '__main__':
    pytest.main()
