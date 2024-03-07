---
abstract: The slice an array problem from HackerRank.
authors: Xander Harris
date: 2024-03-06
title: Slice an Array
---

[![Slice an Array | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=Slice%20an%20Array)](https://www.hackerrank.com/challenges/bash-tutorials-slice-an-array/problem?isFullScreen=true)

## Problem

Given a list of countries, each on a new line, your task is to read them into
an array. Then slice the array and display only the elements lying between
positions $3$ and $7$, both inclusive. Indexing starts from from $0$.

### Input Format

A list of country names. The only characters present in the country names will
be upper or lower case characters and hyphens.

### Output Format

Display the sliced portion of the array of country names, with a space
between each of them.

### Sample Input

```{code-block} shell
Namibia
Nauru
Nepal
Netherlands
NewZealand
Nicaragua
Niger
Nigeria
NorthKorea
Norway
```

### Sample Output

```{code-block} shell
Netherlands NewZealand Nicaragua Niger Nigeria
```

### Explanation

We displayed the sliced portion of the array.

## Solution

```{literalinclude} slice-an-array.sh
:language: shell
:caption: slice-an-array.sh
```

```{index} shell; arrays; slicing
```

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>
```
