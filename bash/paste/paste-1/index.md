---
abstract: The first `paste` problem from HackerRank.
authors: Xander Harris
date: 2024-03-04
title: paste 1
---

[![paste 1 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=paste%201)](https://www.hackerrank.com/challenges/paste-1/)

## Problem

[Paste - 1](https://www.hackerrank.com/challenges/paste-1/)

In this challenge, we practice using the paste command to merge lines of a given file.

You are given a CSV file where each row contains the name of a city and its
state separated by a comma. Your task is to replace the newlines in the file
with semicolons as demonstrated in the sample.

### Input Format

You are given a CSV file where each row contains the name of a city and its state separated by a comma.

### Output Format

Replace the newlines in the input file with semicolons as demonstrated in the sample.

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
Albany, N.Y.;Albuquerque, N.M.;Anchorage, Alaska;Asheville, N.C.;Atlanta, Ga.;Atlantic City, N.J.;Austin, Texas;Baltimore, Md.;Baton Rouge, La.;Billings, Mont.;Birmingham, Ala.;Bismarck, N.D.;Boise, Idaho;Boston, Mass.;Bridgeport, Conn.
```

### Explanation

The delimiter between consecutive rows of data has been transformed from the newline to a semicolon.

## Solution

```{literalinclude} paste-1.sh
:language: shell
:caption: paste-1.sh
```

```{index} paste; replace newlines with semi-colons
```
