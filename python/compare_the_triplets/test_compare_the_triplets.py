""" "Test module for compare the triplets.

Because this particular challenge was solved using an object and the author
is far too lazy to bother with pytest session scope the values
in the PyTest session are cumulative.
"""

import pytest
from compare_the_triplets.compare_the_triplets import ScoreCompare
from compare_the_triplets.compare_the_triplets import compare_triplets


def test_score_compare_initialization():
    """Validate object init."""
    score_compare = ScoreCompare([1, 2, 3], [4, 5, 6])
    assert score_compare.a == [1, 2, 3]
    assert score_compare.b == [4, 5, 6]
    assert score_compare.scores == [0, 0]


def test_score_compare_compare_method():
    """Test sore comparison method."""
    score_compare = ScoreCompare([], [])
    score_compare.compare(3, 2)
    assert score_compare.scores == [1, 0]

    score_compare.compare(1, 5)
    assert score_compare.scores == [1, 1]

    score_compare.compare(8, 2)
    assert score_compare.scores == [2, 1]


def test_score_compare_report_score_method():
    """Test score report method."""
    score_compare = ScoreCompare([], [])
    assert score_compare.report_score() == [2, 1]

    score_compare.compare(3, 2)
    assert score_compare.report_score() == [3, 1]


def test_compare_triplets():
    """Test compare triplets function."""
    assert compare_triplets([1, 2, 3], [4, 5, 6]) == [3, 4]
    assert compare_triplets([5, 6, 7], [3, 2, 1]) == [6, 4]
    assert compare_triplets([2, 2, 2], [1, 1, 1]) == [9, 4]


if __name__ == "__main__":
    pytest.main()
