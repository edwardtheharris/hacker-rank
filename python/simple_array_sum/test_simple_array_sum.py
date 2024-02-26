"""Tests for the simple array sum."""

import pytest
from .simple_array_sum import simple_array_sum

def test_empty_list():
    """Test an empty list."""
    assert simple_array_sum([]) == 0

def test_single_element():
    """Test a single element array."""
    assert simple_array_sum([5]) == 5

def test_positive_numbers():
    """Test that positive numbers work."""
    assert simple_array_sum([1, 2, 3, 4, 5]) == 15

def test_negative_numbers():
    """Test that negative numbers work."""
    assert simple_array_sum([-1, -2, -3, -4, -5]) == -15

def test_mixed_numbers():
    """Test validity of mixed numbers."""
    assert simple_array_sum([-1, 2, -3, 4, -5]) == -3

def test_large_numbers():
    """Test validity of large numbers."""
    assert simple_array_sum([10**6, 10**6, 10**6]) == 3 * 10**6

def test_mixed_types():
    """Test that we've caught the right exceptions."""
    with pytest.raises(TypeError):
        simple_array_sum([1, 2, '3'])

if __name__ == '__main__':
    pytest.main()
