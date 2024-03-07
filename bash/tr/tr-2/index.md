---
abstract: The second `tr` problem from HackerRank.
authors: Xander Harris
date: 2024-03-04
title: tr 2
---

[![tr 2 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=tr%202)](https://www.hackerrank.com/challenges/text-processing-tr-2)

## Problem

In this challenge, we practice using the tr command because it is a useful translation tool in Linux.

In a given fragment of text, delete all the lowercase characters $a-z$.

### Input Format

A block of [ASCII](https://en.wikipedia.org/wiki/ASCII) text.

### Output Format

Delete all the lowercase characters in the given block of text.

### Sample Input

```{code-block} shell
Hello
World
how are you
```

### Sample Output

```{code-block} shell
H
W
```

## Solution

```{literalinclude} tr-2.sh
:language: shell
:caption: tr-2.sh
```

```{index} tr; delete lowercase letters
```
