#!/usr/bin/env python3.13
"""A solution to the HackerRank staircase problem in Python."""

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(n):
    # Write your code here
    for i in range(1, n + 1):
        print(f"{i}")


if __name__ == "__main__":
    n = int(input().strip())

    staircase(n)
