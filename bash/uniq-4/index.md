---
abstract: The Uniq Command 4 problem from HackerRank.
authors: Xander Harris
date: 2024-03-06
title: Uniq Command 4
---

[![Uniq Command 4 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=uniq%204)](https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-4/)

## Problem

[Uniq Command 4](https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-4/problem?isFullScreen=true)

Given a text file, display only those lines that are not followed or preceded by identical replications.

### Sample Input

```{code-block} shell
A00
a00
01
01
00
00
02
02
A00
03
aa
aa
aa
```

### Sample Output

```{code-block} shell
A00
a00
A00
03
```

### Explanation

The comparison is case sensitive, so the first instance of "A00" and "a00" are considered different, hence unique.
The next instance of A00 is succeeded and preceded by different lines, so that is also included in the output.
The same holds true for 03 - it is succeeded and preceded by different lines, so that is also included in the output.

## Solution

```{literalinclude} uniq-4.sh
:language: shell
:caption: uniq-4.sh
```

```{index} single; shell: uniq
```
