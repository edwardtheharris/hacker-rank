---
abstract: The first `sort` problem from HackerRank.
authors: Xander Harris
date: 2024-03-04
title: sort 4
---

[![sort 4 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=sort%204)](https://www.hackerrank.com/challenges/text-processing-sort-4)

## Problem

You are given a file of text, where each line contains a number (which may be either an integer or have decimal places). There will be no extra characters other than the number or the newline at the end of each line. Sort the lines in descending order - - such that the first line holds the (numerically) largest number and the last line holds the (numerically) smallest number.

### Input Format

A text file where each line contains a number as described above.

### Output Format

The text file, with lines re-ordered in descending order (numerically).

### Sample Input

```{code-block} shell
9.1
43.7
2.2
62.1
2.1
9.3
43.5
4.6
44.6
4.7
42.7
47.4
46.6
4.5
55.6
4
9.2
66.6
2
2.3
```

### Sample Output

```{code-block} shell
66.6
62.1
55.6
47.4
46.6
44.6
43.7
43.5
42.7
9.3
9.2
9.1
4.7
4.6
4.5
4
2.3
2.2
2.1
2
```

## Solution

```{literalinclude} sort-4.sh
:language: shell
:caption: sort-4.sh
```
