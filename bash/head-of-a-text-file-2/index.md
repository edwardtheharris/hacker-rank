---
abstract: The second head of a text file problem from HackerRank.
authors: Xander Harris
date: 2024-02-29
title: Head of a Text File 2
---

[![Head of a Text File #2 | HackerRank](https://img.shields.io/badge/Head%20of%20a%20Text%20File%202-green?style=for-the-badge&logo=hackerrank&label=HackerRank)](https://www.hackerrank.com/challenges/text-processing-head-2/)

## Problem

In this challenge, we practice using the [head](https://www.mankier.com/1/head)
command to display the first $20$ characters of a text file.

Display the first $20$ characters of an input file.

### Input Format

A text file.

### Output Format

Output the first $20$ characters of the text file.

### Sample Input

```{card} Sample Input
 New York is a state in the Northeastern and Mid-Atlantic regions of the United States.
New York is the 27th-most extensive, the third-most populous populated of the 50 United States.
New York is bordered by New Jersey and Pennsylvania to the south.
About one third of all the battles of the Revolutionary War took place in New York.
Henry Hudson's 1609 voyage marked the beginning of European involvement with the area.
```

### Sample Output

```{card} Sample Output
New York is a stat
```

## Solution

```{literalinclude} head-of-a-text-file-2.sh
:language: shell
:caption: head-of-a-text-file-2.sh
```
