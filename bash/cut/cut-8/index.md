---
abstract: The eighth cut problem from HackerRank.
authors: Xander Harris
title: Cut 8
---

[![Cut #8 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=Cut%208)](https://www.hackerrank.com/challenges/text-processing-cut-8/problem?isFullScreen=true)

## Problem

Given a sentence, identify and display its first three words. Assume that the
space (' ') is the only delimiter between words.

### Input Format

A text file with lines of ASCII text only. Each line has exactly one sentence.

### Constraints

- $1 \le N \le 100$

($N$ is the number of lines of text in the input file)

### Output Format

The output should contain $N$ lines. For each input sentence, identify
and display its first three words. Assume that the space (' ') is the only
delimiter between words.

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
New York is<br />
New York is<br />
New York is<br />
About one third<br />
Henry Hudson's 1609<br />
```

## Solution

```{literalinclude} cut-8.sh
:language: shell
:caption: cut-8.sh
```

```{index} cut; print specific words
```
