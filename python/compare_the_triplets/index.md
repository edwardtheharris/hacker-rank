---
abstract: >-
    Alice and Bob each created one problem for HackerRank. A reviewer rates the
    two challenges, awarding points on a scale from 1 to 100 for three
    categories: problem clarity, originality, and difficulty.
authors: Xander Harris
date: 2024-02-19
title: Compare the Triplets
---

The rating for Alice's challenge is the triplet
`a = (a[0], a[1], a[2])`{l=python}, and the rating for Bob's challenge is
the triplet `b = (b[0], b[1], b[2])`{l=python}.

The task is to find their comparison points by comparing `a[0]` with `b[0]`,
`a[1]` with `b[1]`, and `a[2]` with `b[2]`.

If `a[i] > b[i]`, then Alice is awarded 1 point.
If `a[i] < b[i]`, then Bob is awarded 1 point.
If `a[i] = b[i]`, then neither person receives a point.

Comparison points is the total points a person earned.

Given `a` and `b`, determine their respective comparison points.

## Example

```{code-block} python
a = [1, 2, 3]
b = [3, 2, 1]
```

- For elements `0`, Bob is awarded a point because `a[0] < b[0]`{l=python}.
- For elements `1`, there is equality `a[1] = b[1]`{l=python}, no points are earned.
- Finally, for elements 2, `a[2] > b[2]`{l=python} so Alice receives a point.

The return array is `[1, 1]`{l=python} with Alice's score first and Bob's second.

## Function Description

Complete the function `compare_triplets`{l=py} in the editor below.

`compare_triplets`{l=py} has the following parameter(s):

```{eval-rst}
:var list(int) a[3]: Alice's challenge rating
:var list(int) b[3]: Bob's challenge rating
```

Return

```{eval-rst}
:var list(int)[2]: Alice's score is in the first position,
    and Bob's score is in the second.
```

## Input Format

The first line contains 3 space-separated integers, `a[0]`, `a[1]`, and `a[2]`,
the respective values in triplet `a`.
The second line contains 3 space-separated integers, `b[0]`, `b[1]`, and `b[2]`,
the respective values in triplet `b`.

### Constraints

$1 ≤ a[i] ≤ 100$ß

$1 ≤ b[i] ≤ 100$

### Sample Input 0

```{code-block} shell
5 6 7
3 6 10
```

### Sample Output 0

```sh
1 1
```

### Explanation 0

In this example:

- $a = (a[0], a[1], a[2]) = (5, 6, 7)$
- $b = (b[0], b[1], b[2]) = (3, 6, 10)$

Now, let's compare each individual score:

- $a[0] > b[0]$, so Alice receives $1$ point.
- $a[1] = b[1]$, so nobody receives a point.
- $a[2] < a[2]$, so Bob receives $1$ point.

Alice's comparison score is $1$, and Bob's comparison score is $1$.
Thus, we return the array $[1, 1]$.

### Sample Input 1

```{code-block} shell
17 28 30
99 16 8
```

### Sample Output 1

```{code-block} shell
2 1
```

### Explanation 1

- Comparing the $0^{th}$ elements, $17 < 99$ so Bob receives a point.
- Comparing the $1^{st}$ and $2^{nd}$ elements, $28 > 16$ and $30 > 8$ so Alice
  receives two points.

The return array is $[2, 1]$.
