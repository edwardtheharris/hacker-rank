---
abstract: The concatenate an array problem from HackerRank.
authors: Xander Harris
date: 2024-03-07
title: Concatenate an array to itself
---

[![Concatenate an Array to Itself | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=count%20the%20number%20of%20elements%20in%20an%20array)](https://www.hackerrank.com/challenges/bash-tutorials-read-in-an-array/)

## Problem

[Concatenate an Array with Itself](https://www.hackerrank.com/challenges/bash-tutorials-concatenate-an-array-with-itself/problem?isFullScreen=true)

Given a list of countries, each on a new line, your task is to read them into
an array. Then, concatenate the array with itself (twice) - so that you have a
total of three repetitions of the original array - and then display the entire
concatenated array, with a space between each of the countries' names.

### Recommended References

Here's a
[great tutorial](http://www.thegeekstuff.com/2010/06/bash-array-tutorial/)
with useful examples related to arrays in Bash.

### Input Format

A list of country names. The only characters present in the country names
will be upper or lower case characters and hyphens.

### Output Format

Display the entire concatenated array, with a space between each of them.

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
Namibia Nauru Nepal Netherlands NewZealand Nicaragua Niger Nigeria NorthKorea Norway Namibia Nauru Nepal Netherlands NewZealand Nicaragua Niger Nigeria NorthKorea Norway Namibia Nauru Nepal Netherlands NewZealand Nicaragua Niger Nigeria NorthKorea Norway
```

### Explanation

The entire concatenated array has been displayed.

```{admonition} No Newline
The `read` command expects input that ends with a newline, which is not provided
in this challenge, so the solution is considerably more complicated
than would otherwise be necessary.
```

## Solution

```{literalinclude} concatenate-an-array-to-itself.sh
:language: shell
:caption: concatenate-an-array-to-itself.sh
```

```{index} arrays; concatenation
```
