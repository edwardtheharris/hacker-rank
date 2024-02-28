---
abstract: The eighth cut problem from HackerRank.
authors: Xander Harris
title: Cut 8
---

[![Cut #8 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=Cut%208)](https://www.hackerrank.com/challenges/text-processing-cut-8/problem?isFullScreen=true)

## Problem

Given a sentence, identify and display its first three words. Assume that the space (' ') is the only delimiter between words.

### Input Format

A text file with lines of ASCII text only. Each line has exactly one sentence.

### Constraints

- $1 \le N \le 100$

($N$ is the number of lines of text in the input file)

### Output Format

The output should contain $N$ lines. For each input sentence, identify and display its first three words. Assume that the space (' ') is the only delimiter between words.

### Sample Input

```sh
New York is a state in the Northeastern and Mid-Atlantic regions of the United States.
New York is the 27th-most extensive, the third-most populous populated of the 50 United States.
New York is bordered by New Jersey and Pennsylvania to the south.
About one third of all the battles of the Revolutionary War took place in New York.
Henry Hudson's 1609 voyage marked the beginning of European involvement with the area.
```

### Sample Output

```sh
New York is
New York is
New York is
About one third
Henry Hudson's 1609
```

## Solution

```{literalinclude} cut-8.sh
:language: shell
:caption: cut-8.sh
```
