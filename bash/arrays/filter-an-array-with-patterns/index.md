---
abstract: The shell array filtering problem from HackerRank.
authors:
    - name: Xander Harris
      email: xandertheharris@gmail.com
date: 2024-03-04
title: Filter an Array with Patterns
---

## Overview

[![Filter an Array with Patterns | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=Filter%20an%20Array%20with%20Patterns)](https://www.hackerrank.com/challenges/bash-tutorials-filter-an-array-with-patterns/problem?isFullScreen=true)

### Objective

We now transition to some basic examples of bash scripting for the purpose of
text processing and data munging. In this challenge, we practice reading and
filtering an array.

### Resources

Here's a great tutorial with useful examples related to arrays in Bash.

### Task

You are given a list of countries, each on a new line. Your task is to read
them into an array and then filter out (remove) all the names containing the
letter 'a' or 'A'.

#### Input Format

The input format consists of a list of country names, each on a separate line.
The only characters present in the country names will be upper or lower case
characters and hyphens.

#### Output Format

From the given list, remove the names that contain 'a' or 'A' in them. If there
are no names left after removing these characters, you should display a blank
line.

#### Sample Input

```{code-block} text
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

#### Sample Output

```{code-block} text
Niger
```

## Explanation

Niger is the only name that does not contain an 'a' or 'A'.

## Solution

```{literalinclude} filter-array.sh
:language: shell
```
