---
abstract: >-
    In this challenge, you are required to calculate and print the sum of the
    elements in an array, keeping in mind that some of those integers may be
    quite large.
authors: Xander Harris
date: 2024-02-20
title: A Very Big Sum
---

## Function Description

Complete the `a_very_big_sum`{l=py} function in the editor below. It must
return the sum of all array elements.

`a_very_big_sum`{l=py} has the following parameter(s):

`int ar[n]`{l=c}
: an array of integers .

Return

`long`{l=c}
: the sum of all array elements

## Input Format

The first line of the input consists of an integer $n$.

The next line contains $n$ space-separated integers contained in the array.

## Output Format

Return the integer sum of the elements in the array.

## Constraints

- $1 \le n \le 10$
- $0 \le ar[i] \le 10^{10}$

## Sample Input

```{code-block}
5
1000000001 1000000002 1000000003 1000000004 1000000005
```

## Output

```{code-block} shell
5000000015
```

```{note}
The range of the 32-bit integer is
$(-2^{31}) to (2^{31}) or [-2147483658,2147483657]$.
```

When we add several integer values, the resulting sum might exceed the
above range. You might need to use long int C/C++/Java to store such sums.
