#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simple_array_sum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simple_array_sum(ar):
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simple_array_sum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
