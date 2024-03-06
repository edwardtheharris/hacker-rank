---
abstract: The third `tr` problem from HackerRank.
authors: Xander Harris
date: 2024-03-04
title: tr 3
---

[![tr 3 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=tr%203)](https://www.hackerrank.com/challenges/text-processing-tr-3)

## Problem

In a given fragment of text, replace all sequences of multiple spaces with just one space.

### Input Format

A block of ASCII text.

### Output Format

Replace all sequences of multiple spaces with just one space.

### Sample Input

```{code-block} shell
He  llo
Wor  ld
how  are  you
```

### Sample Output

```{code-block} shell
He llo
Wor ld
how are you
```

## Solution

```{literalinclude} tr-3.sh
:language: shell
:caption: tr-3.sh
```
