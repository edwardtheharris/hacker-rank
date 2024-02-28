---
abstract: The first `cut` problem from HackerRank.
authors: Xander Harris
title: Cut #1
---

## Problem

Given $N$ lines of input, print the $3rd$ character from each line as a new
line of output. It is guaranteed that each of the lines of input will
have a $3rd$ character.

### Input Format

A text file containing $N$ lines of ASCII characters.

### Constraints

- $1 \le N \le 100$

### Output Format

For each line of input, print its
character on a new line for a total of

lines of output.

### Sample Input

```{code-block} shell
Hello
World
how are you
```

### Sample Output

```{code-block} shell
l
r
w
```

## Solution

```{literalinclude} cut-1.sh
:language: shell
:caption: cut-1.sh
```
