---
abstract: The second tail of a text file problem from HackerRank.
authors: Xander Harris
title: Tail of a Text File 2
---

[![Tail of a Text File 2 | HackerRank](https://img.shields.io/badge/Tail%20of%20a%20Text%20File%202-green?style=for-the-badge&logo=hackerrank&label=HackerRank)](https://www.hackerrank.com/challenges/text-processing-tail-2/)

## Problem

In this challenge, we practice using the [tail](https://www.mankier.com/1/tail)
command to display the last $20$ characters of a text file.

Display the last $20$ characters of an input file.

### Input Format

A text file.

### Output Format

Output the last $20$ characters of the text file.

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
ent with the area.
````

## Solution

```{literalinclude} tail-of-a-text-file-2.sh
:language: shell
:caption: tail-of-a-text-file-2.sh
```
