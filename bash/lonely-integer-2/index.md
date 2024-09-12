---
abstract: The first `sort` problem from HackerRank.
authors: Xander Harris
date: 2024-03-04
title: Lonely Integer
---

[![Lonely Integer | HackerRank](https://img.shields.io/badge/HackerRank-green?style=for-the-badge&logo=hackerrank&label=Lonely%20Integer)](https://www.hackerrank.com/challenges/lonely-integer-2/problem)

## Overview

There are $N$ integers in an array $A$. All but one integer occur in pairs.
Your task is to find the number that occurs only once.

### Input Format

The first line of the input contains an integer $N$, indicating the number of
integers. The next line contains $N$ space-separated integers that form
the array $A$.

### Constraints

$1 \leq N < 100$

$N \% 2 = 1$ ($N$ is an odd number)

$0 \leq A[i] \leq 100, \forall \epsilon [1,N]$

### Output Format

Output , the number that occurs only once.

#### Sample Input:1

```{code-block} shell
1
1
```

#### Sample Output:1

```{code-block} shell
1
```

#### Sample Input:2

```{code-block} shell
3
1 1 2
```

#### Sample Output:2

```{code-block} shell
2
```

#### Sample Input:3

```{code-block} shell
5
0 0 1 2 1
```

#### Sample Output:3

```{code-block} shell
2
```

### Explanation

In the first input, we see only one element (1) and that element is the
answer.

In the second input, we see three elements; 1 occurs at two places and 2 only
once. Thus, the answer is 2.

In the third input, we see five elements. 1 and 0 occur twice. The element
that occurs only once is 2.

## Solution

```{literalinclude} lonely-integer.sh
:language: shell
:caption: lonely-integer.sh
```

```{index} array; shell
```
