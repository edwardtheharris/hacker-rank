---
abstract: The first `sort` problem from HackerRank.
authors: Xander Harris
date: 2024-03-04
title: sort 1
---

[![sort 1 | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=sort%201)](https://www.hackerrank.com/challenges/text-processing-sort-1)

## Problem

In this challenge, we practice using the sort command to sort input in text or TSV formats.

Given a text file, order the lines in lexicographical order.

### Input Format

A text file.

### Output Format

Output the text file with the lines reordered in lexicographical order.

### Sample Input

```{code-block} shell
Dr. Rajendra Prasad     January 26, 1950    May 13, 1962
Dr. S. Radhakrishnan        May 13, 1962    May 13, 1967
Dr. Zakir Hussain       May 13, 1967    August 24, 1969
Shri Varahagiri Venkata Giri        August 24, 1969 August 24, 1974
Shri Fakhruddin Ali Ahmed       August 24, 1974 February 11, 1977
Shri Neelam Sanjiva Reddy       July 25, 1977   July 25, 198
```

### Sample Output

```{code-block} shell
Dr. Rajendra Prasad     January 26, 1950    May 13, 1962
Dr. S. Radhakrishnan        May 13, 1962    May 13, 1967
Dr. Zakir Hussain       May 13, 1967    August 24, 1969
Shri Fakhruddin Ali Ahmed       August 24, 1974 February 11, 1977
Shri Neelam Sanjiva Reddy       July 25, 1977   July 25, 198
Shri Varahagiri Venkata Giri        August 24, 1969 August 24, 1974
```

## Solution

```{literalinclude} sort-1.sh
:language: shell
:caption: sort-1.sh
```
