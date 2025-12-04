#!/usr/bin/env python3.13
from sys import argv


def staircase(steps):
    """Implement a solution to the staircase problem."""
    steps = steps + 1
    for i in range(1, steps):
        k = steps - i
        sp = " " * k
        st = "#" * i
        output = f"{sp}{st}"
        print(output[1:])


if __name__ == "__main__":
    n = int(argv[1])
    staircase(n)
