---
abstract: The sixth cut problem from HackerRank.
authors: Xander Harris
title: Cut 6
---

[![Cut #6 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=Cut%206)](https://www.hackerrank.com/challenges/text-processing-cut-6/problem?isFullScreen=true)

## Problem

Print the characters from the thirteenth position to the end.

### Input Format

A text file with lines of ASCII text only.

### Constraints

- $1 \le N \le 100$

($N$ is the number of lines of text in the input file)

### Output Format

The output should contain $N$ lines. For each input line, print the characters from the thirteenth position to the end.

### Sample Input

```{card} Sample Input
New York is a state in the Northeastern and Mid-Atlantic regions of the United States.<br />
New York is the 27th-most extensive, the third-most populous populated of the 50 United States.<br />
New York is bordered by New Jersey and Pennsylvania to the south.<br />
About one third of all the battles of the Revolutionary War took place in New York.<br />
Henry Hudson's 1609 voyage marked the beginning of European involvement with the area.<br />
```

### Sample Output

```{card} Sample Output
a state in the Northeastern and Mid-Atlantic regions of the United States.<br />
the 27th-most extensive, the third-most populous populated of the 50 United States.<br />
bordered by New Jersey and Pennsylvania to the south.<br />
ird of all the battles of the Revolutionary War took place in New York.<br />
's 1609 voyage marked the beginning of European involvement with the area.<br />
```

## Solution

```{literalinclude} cut-6.sh
:language: shell
:caption: cut-6.sh
```
