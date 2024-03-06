---
abstract: The seventh cut problem from HackerRank.
authors: Xander Harris
title: Cut 7
---

[![Cut #7 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=Cut%207)](https://www.hackerrank.com/challenges/text-processing-cut-7/problem?isFullScreen=true)

## Problem

Given a sentence, identify and display its fourth word. Assume that the space (' ') is the only delimiter between words.

### Input Format

A text file with lines of ASCII text only. Each line has exactly one sentence.

### Constraints

- $1 \le N \le 100$

($N$ is the number of lines of text in the input file)

### Output Format

The output should contain $N$ lines.

For each input sentence, identify and display its fourth word. Assume that the space (' ') is the only delimiter between words.

### Sample Input

```sh
Hello
World
how are you
```

### Sample Output

```sh
Hello
World
```

## Solution

```{literalinclude} cut-7.sh
:language: shell
:caption: cut-7.sh
```
