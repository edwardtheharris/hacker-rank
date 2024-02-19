---
abstract: Given an array of integers, find the sum of its elements.
authors: Xander Harris
date: 2024-02-19
title: Simple Array Sum
---

```{note}
This was adapted from the Hacker Rank challenge available
[here](https://www.hackerrank.com/challenges/simple-array-sum/problem).
```

Given an array of integers, find the sum of its elements.

For example, if the array $ar = [1,2,3]$, $1 + 2 + 3 = 6$, so return $6$.

## Function Description

Complete the simple_array_sum function in the editor below. It must return
the sum of the array elements as an integer.

`simple_array_sum`{l=python} has the following parameter(s):

- `list(ar)`{l=python} an array of integers

## Input Format

The first line contains an integer, $n$, denoting the size of the array.
The second line contains $n$ space-separated integers representing the array's
elements.

## Constraints

$0<N,ar[i]\le1000$

## Output Format

Print the sum of the array's elements as a single integer.

## Sample Input

```{code-block} shell
6
1 2 3 4 10 11
```

## Sample Output

```{code-block} shell
31
```

## Explanation

We print the sum of the array's elements: $1 + 2 + 3 + 4 + 10 + 11 = 31$.

## Python Solution Docs

```{eval-rst}
.. currentmodule:: simple_array_sum

.. automodule:: simple_array_sum
   :members:
```

### simple array sum

- [simple_array_sum.py](simple_array_sum.py)

```{literalinclude} simple_array_sum.py
:language: python
```

### SCM

Available in the related
[GitHub issue](https://github.com/edwardtheharris/hacker-rank/issues/6).

````{figure} /_static/img/simple_array_sum/solved.jpeg
```{sectionauthor} Xander Harris <xandertheharris@gmail.com>
```
````
