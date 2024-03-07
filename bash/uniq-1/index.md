---
abstract: The Uniq Command 1 problem from HackerRank.
authors: Xander Harris
date: 2024-03-05
title: Uniq Command 1
---

[![Uniq Command 1 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=uniq%201)](https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-1)

## Problem

[Uniq Command 1](https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-1/problem?isFullScreen=true)

In this challenge, we practice using the uniq command to eliminate consecutive repetitions of a line when a text file is piped through it.

Given a text file, remove the consecutive repetitions of any line.

### Sample Input

```{code-block} shell
00
00
01
01
00
00
02
02
```

### Sample Output

```{code-block} shell
00
01
00
02
```

## Solution

```{literalinclude} uniq-1.sh
:language: shell
:caption: uniq-1.sh
```
