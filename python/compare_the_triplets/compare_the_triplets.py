#!/usr/bin/env python3
"""This module contains a function to compare triplet values."""

import os
import pathlib


class ScoreCompare:
    """Define a ScoreCompare object.

    :attribute list a: An empty list.
    :attribute list b: Another empty list.
    :attribute list scores: A list with two values initialized to 0.
    """

    a = []
    b = []
    scores = [0, 0]

    def __init__(self, a_list, b_list):
        self.a = a_list
        self.b = b_list

    def compare(self, a_int, b_int):
        """Compare values for two integers.

        :param int a_int: An integer value
        :param int b_int: Another integer value
        """
        if a_int > b_int:
            self.scores[0] += 1
        elif a_int < b_int:
            self.scores[1] += 1

    def report_score(self):
        """Report the current score."""
        return self.scores


def compare_triplets(a_trip, b_trip):
    """Compare sets of triplets to provide a score.

    :param list a_trip: INTEGER_ARRAY a, contains 3 values
    :param list b_trip: INTEGER_ARRAY b, contains 3 values
    :return: The function is expected to return an INTEGER_ARRAY with 2 values.
    """
    sc_obj = ScoreCompare(a_trip, b_trip)

    for index, value in enumerate(a_trip):
        sc_obj.compare(value, b_trip[index])

    return sc_obj.scores


if __name__ == "__main__":
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compare_triplets(a, b)

    fpath = pathlib.Path(os.environ.get("OUTPUT_PATH"))
    with fpath.open("w", encoding="utf-8") as fp_handle:
        fp_handle.write(" ".join(map(str, result)))
        fp_handle.write("\n")
