---
abstract: This code implements a solution to the described problem in Python.
title: Staircase in Python
---

## [Staircase.Python](https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true)

```{note}
See
[GitHub Issue #109](https://github.com/edwardtheharris/hacker-rank/issues/109)
```

### Staircase detail

This is a staircase of size $n = 4$:

```shell
   #
  ##
 ###
####
```

Its base and height are both equal to $n$. It is drawn using `#` symbols and
spaces. **The last line is not preceded by any spaces**.

Write a program that prints a staircase of size $n$.

### Function Description

Complete the *staircase* with the following parameter(s):

* *int n*: an integer

### Print

Print a staircase as described above.

```text
The last line is not preceded by spaces. All lines are right-aligned.
```

### Input Format

A single integer, $n$, denoting the size of the staircase.

Constraints

 $0 \lt n \leq 100$.

### Sample Input

`6`

### Sample Output

```shell
     #
    ##
   ###
  ####
 #####
######
```

### Explanation

The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of $n=6$.

[python.print](https://docs.python.org/3/library/functions.html#print)

## Solved

```{figure} Staircase.HackerRank.png
:caption: 2025-12-04
```
