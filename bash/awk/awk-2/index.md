---
abstract: >-
  A program that you can use to select particular records in a file and
  perform operations upon them.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-09-04
title: awk command 2
---

[![awk #2](https://img.shields.io/badge/awk_%232-hackerrank?style=flat&logo=hackerrank&label=HackerRank)](https://www.hackerrank.com/challenges/awk-2/problem?isFullScreen=true)

## Objective

In this challenge, we practice using the {term}`awk` command for text-munging
and data processing tasks.

### Resources

The awk interpreter may be used for a lot of text-munging and
data-processing tasks that require some quick scripting work.

The following links show examples with {term}`awk`:

- [Print Examples](http://www.thegeekstuff.com/2010/01/awk-introduction-tutorial-7-awk-print-examples/)
- [Conditionals with Awk](http://www.thegeekstuff.com/2010/02/awk-conditional-statements/)

## Task

You are given a file with four space separated columns containing the scores
of students in three subjects. The first column contains a single character
($A-Z$), the student identifier. The next three columns have three numbers
each. The numbers are between $0$ and $100$, both inclusive. These numbers
denote the scores of the students in English, Mathematics, and Science,
respectively.

Your task is to identify whether each of the students has passed or failed.
A student is considered to have passed if (s)he has a score $50$ or more in
each of the three subjects.

### Input Format

There will be no more than $10$ rows of data.

Each line will be in the following format:

`[Identifier][English Score][Math Score][Science Score]`

### Output Format

Depending on the scores, display the following for each student:

`[Identifier] : [Pass]`

or

`[Identifier] : [Fail]`

### Sample Input

```{epigraph}
A 25 27 50
B 35 37 75
C 75 78 80
D 99 88 76
```

### Sample Output

```{epigraph}
A : Fail
B : Fail
C : Pass
D : Pass
```

### Explanation

Only student C and student D have scored $\geq 50$ in all three subjects.

## Solution

Here we compute the average score for three grades then assign and print
a pass or fail grade to that score.

```{literalinclude} /bash/awk/awk-2/awk-2.sh
:language: shell
```
