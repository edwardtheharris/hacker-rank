#!/bin/python3
"""This module calculates a large sum.
#
# Complete the 'a_very_big_sum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#
"""

import os
import pathlib


def a_very_big_sum(ar_to_sum):
    """Calculate a very big sum.

    :param list ar_to_sum: A list of integers to add up.
    :return: The sum of the integers contained in the array.
    """
    try:
        ret_sum = 0
        for value in ar_to_sum:
            ret_sum = ret_sum + value
    except TypeError as type_error:
        raise TypeError("Please supply numeric values.") from type_error
    return ret_sum


if __name__ == "__main__":

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = a_very_big_sum(ar)

    fpath = pathlib.Path(os.environ.get("OUTPUT_PATH"))
    with fpath.open("w", encoding="utf-8") as f_handle:
        f_handle.write(str(result) + "\n")
