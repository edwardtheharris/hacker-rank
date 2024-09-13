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

In this challenge, we practice reading and transforming arrays.

### Resources

Here's a great
[tutorial](http://www.thegeekstuff.com/2010/06/bash-array-tutorial/)
with useful examples related to arrays in Bash.

## Task

You are given a list of countries, each on a new line. Your task is to read
them into an array and then transform them in the following way:

The first capital letter (if present) in each element of the array should be
replaced with a dot ('.'). Then, display the entire array with a
space between each country's names.

### Input Format

The input format consists of a list of country names each on a separate line.
The only characters present in the country names will be upper or lower case
characters and hyphens.

### Output Format

Transform the names as described and display the entire array of country
names with a space between each of them.

### Sample Input

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

### Sample Output

```{code-block} text
.amibia .auru .epal .etherlands .ewZealand .icaragua .iger .igeria .orthKorea .orway
```

Explanation

The first capital letter of each name has been replaced with a dot ('.').
