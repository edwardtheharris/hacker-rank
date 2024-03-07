---
abstract: The second cut problem from HackerRank.
authors: Xander Harris
title: Cut 2
---

[![Cut #2 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=Cut%202)](https://www.hackerrank.com/challenges/text-processing-cut-2/problem?isFullScreen=true)

## Problem

Display the $2^{nd}$ and $7^{th}$ character from each line of text.

### Input Format

A text file with $N$ lines of ASCII text only.

### Constraints

- $1 \le N \le 100$

### Output Format

The output should contain $N$ lines. Each line should contain just two characters at the $2^{nd}$ and the $7^{th}$ position of the corresponding input line.

### Sample Input

```{code-block} shell
Hello

World

how are you
```

### Sample Output

```{code-block} shell
e

o

oe
```

## Solution

```{literalinclude} cut-2.sh
:language: shell
:caption: cut-2.sh
```

```{index} cut; print specific characters from a line
```
