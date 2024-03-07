---
abstract: The fourth cut problem from HackerRank.
authors: Xander Harris
title: Cut 4
---

[![Cut #4 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=Cut%204)](https://www.hackerrank.com/challenges/text-processing-cut-4/problem?isFullScreen=true)

## Problem

Display the first four characters from each line of text.

### Input Format

A text file with lines of ASCII text only.

### Constraints

- $1 \le N \le 100$

($N$ is the number of lines of text in the input file)

### Output Format

The output should contain $N$ lines. Each line should contain just the first four characters of the corresponding input line.

### Sample Input

```{code-block} shell
Hello
World
how are you
```

### Sample Output

```{code-block} shell
Hell
Worl
how
```

## Solution

```{literalinclude} cut-4.sh
:language: shell
:caption: cut-4.sh
```

```{index} cut; print the beginning of a line of text
```
