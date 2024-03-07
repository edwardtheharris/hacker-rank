---
abstract: The first `tr` problem from HackerRank.
authors: Xander Harris
date: 2024-03-04
title: tr 1
---

[![tr 1 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=tr%201)](https://www.hackerrank.com/challenges/text-processing-tr-1)

## Problem

In this challenge, we practice using the tr command because it is a useful translation tool in Linux.

In a given fragment of text, replace all parentheses `()` with box brackets `[]`.

### Input Format

A block of [ASCII](https://en.wikipedia.org/wiki/ASCII) text.

### Output Format

Output the text with all parentheses `()` replaced with box brackets `[]`.

### Sample Input

```{code-block} shell
int i=(int)5.8
(23 + 5)*2
```

### Sample Output

```{code-block} shell
int i=[int]5.8
[23 + 5]*2
```

## Solution

```{literalinclude} tr-1.sh
:language: shell
:caption: tr-1.sh
```

```{index} shell: tr-1
```
