---
abstract: The third cut problem from HackerRank.
authors: Xander Harris
title: Cut 3
---

[![Cut #3 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=Cut%203)](https://www.hackerrank.com/challenges/text-processing-cut-3/problem?isFullScreen=true)

## Problem

Display a range of characters starting at the $2^{nd}$ position of a string and ending at the $7^{th}$ position (both positions included).

### Input Format

A text file containing $N$ lines of [ASCII](https://en.wikipedia.org/wiki/ASCII) text only.

### Constraints

- $1 \le N \le 100$

### Output Format

The output should contain $N$ lines.
Each line should contain the range of characters starting at the $2^{nd}$ position of a string and ending at the $7^{th}$ position (both positions included).

### Sample Input

```{code-block} shell
Hello
World
how are you
```

### Sample Output

```{code-block} shell
ello
orld
ow are
```

## Solution

```{literalinclude} cut-3.sh
:language: shell
:caption: cut-3.sh
```

```{index} cut; print a range of characters from a line
```
