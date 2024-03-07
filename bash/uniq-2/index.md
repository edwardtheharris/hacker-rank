---
abstract: The Uniq Command 2 problem from HackerRank.
authors: Xander Harris
date: 2024-03-05
title: Uniq Command 2
---

[![Uniq Command 2 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=uniq%202)](https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-2/)

## Problem

[Uniq Command 2](https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-2/problem?isFullScreen=true)

In this challenge, we practice using the uniq command to eliminate consecutive repetitions of a line when a text file is piped through it.

Given a text file, count the number of times each line repeats itself. Only consider consecutive repetitions. Display the space-separated count and line, respectively. There shouldn't be any leading or trailing spaces. Please note that the uniq -c command by itself will generate the output in a different format than the one expected here.

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
03
aa
aa
aa
```

### Sample Output

```{code-block} shell
2 00
2 01
2 00
2 02
1 03
3 aa
```

### Explanation

```{code-block} shell
00 is repeated twice
01 is repeated twice
00 is repeated twice
02 is repeated twice
03 occurs once
aa is repeated thrice
```

## Solution

```{literalinclude} uniq-2.sh
:language: shell
:caption: uniq-2.sh
```

```{index} command; uniq-2
```

```{index} shell; uniq-2
```
