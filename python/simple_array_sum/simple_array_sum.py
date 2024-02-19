#!/usr/bin/env python3
"""A simple module that prints the sum of an array of integers."""

import pathlib
import os
# import random
# import re
# import sys

#
# Complete the 'simple_array_sum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simple_array_sum(ar_list):
    """Sum the contents of an array."""
    ret_value = sum(ar_list[1:])
    return ret_value

if __name__ == '__main__':
    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simple_array_sum(ar)

    fpath = pathlib.Path(os.environ.get('OUTPUT_PATH'))
    with fpath.open('w', encoding='utf-8') as f_handle:
        f_handle.write(str(result) + '\n')
