---
abstract: >-
  A program that you can use to select particular records in a file and
  perform operations upon them.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-09-04
title: awk command 4
---

[![awk #4](https://img.shields.io/badge/awk_%234-hackerrank?style=flat&logo=hackerrank&label=HackerRank)](https://www.hackerrank.com/challenges/awk-3/problem?isFullScreen=true)

## An Introduction to {term}`awk`

There are a lot of quick tricks which may be accomplished with the {term}`awk`
interpreter. Among other things, awk may be used for a lot of text-munging
and data-processing tasks which require some quick scripting work.

Examples with awk

- [Print Examples](http://www.thegeekstuff.com/2010/01/awk-introduction-tutorial-7-awk-print-examples/)
- [Conditionals with Awk](http://www.thegeekstuff.com/2010/02/awk-conditional-statements/)

```{note}
Only solutions using awk will be considered valid for this task
```

## Task

You are provided a file with four space-separated columns containing the scores
of students in three subjects. The first column, contains a single character
(A-Z) - the identifier of the student. The next three columns have three
numbers (each between 0 and 100, both inclusive) which are the scores of the
students in English, Mathematics and Science respectively.

### Input Format

There will be no more than $10$ rows of data. Each line will be in the format:

`[Identifier] [Score in English] [Score in Math] [Score in Science]`

### Output Format

Concatenate every 2 lines of input with a semi-colon.

### Sample Input

```{epigraph}
A 25 27 50
B 35 37 75
C 75 78 80
D 99 88 76
```

### Sample Output

```{epigraph}
A 25 27 50;B 35 37 75
C 75 78 80;D 99 88 76
```

### Explanation

Every pair of lines have been concatenated with a semi-colon.
