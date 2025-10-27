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
    ispace = " "
    ihash = "#"
    ilist = [ispace, ispace, ispace, ispace, ispace, ispace]
    for index, value in enumerate(ilist):
        ilist[:-index] = ihash
        print(ilist)


if __name__ == "__main__":
    n = int(input().strip())

    staircase(n)
