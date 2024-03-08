---
abstract: The third `paste` problem from HackerRank.
authors: Xander Harris
date: 2024-03-07
title: paste 3
---

[![paste 3 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=paste%203)](https://www.hackerrank.com/challenges/paste-3)

## Problem

[Paste - 3](https://www.hackerrank.com/challenges/paste-3/problem?isFullScreen=true)

Given a CSV file where each row contains the name of a city and its state
separated by a comma, your task is to replace the newlines in the file with
tabs as demonstrated in the sample.

### Input Format

You are given a CSV file where each row contains the name of a city and its
state separated by a comma.

### Output Format

Replace the newlines in the input with tabs as demonstrated in the sample.

### Sample Input

```{code-block} shell
Albany, N.Y.
Albuquerque, N.M.
Anchorage, Alaska
Asheville, N.C.
Atlanta, Ga.
Atlantic City, N.J.
Austin, Texas
Baltimore, Md.
Baton Rouge, La.
Billings, Mont.
Birmingham, Ala.
Bismarck, N.D.
Boise, Idaho
Boston, Mass.
Bridgeport, Conn.
```

### Sample Output

```{code-block} shell
Albany, N.Y.    Albuquerque, N.M.   Anchorage, Alaska   Asheville, N.C.Atlanta, Ga. Atlantic City, N.J. Austin, Texas   Baltimore, Md.  Baton Rouge, La.    Billings, Mont. Birmingham, Ala.    Bismarck, N.D.  Boise, Idaho    Boston, Mass.   Bridgeport, Conn.
```

### Explanation

The delimiter between consecutive rows of data has been transformed from the newline to a tab.

## Solution

```{literalinclude} paste-3.sh
:language: shell
:caption: paste-3.sh
```

```{index} paste; replace multiple newlines with tabs
```
