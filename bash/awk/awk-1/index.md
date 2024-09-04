---
abstract: >-
  A program that you can use to select particular records in a file and
  perform operations upon them.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-02-07
title: awk command 1
---

[![awk #1](https://img.shields.io/badge/awk_%231-hackerrank?style=flat&logo=hackerrank&label=HackerRank)](https://www.hackerrank.com/challenges/awk-1/problem?isFullScreen=true)

## Objective

In this challenge, we practice using the {term}`awk` command for text-munging
and data-processing tasks.

### Resources

Here's a useful video on the topic:

```{youtube} az6vd0tGhJI
```

The {term}`awk` interpreter may be used for a lot of text-munging and
data-processing tasks that require some quick scripting work.

The following links show examples with {term}`awk`:

- [Print Examples](http://www.thegeekstuff.com/2010/01/awk-introduction-tutorial-7-awk-print-examples/)
- [Conditionals with Awk](http://www.thegeekstuff.com/2010/02/awk-conditional-statements/)

## Task

You are given a file with four space separated columns containing the scores
of students in three subjects. The first column contains a single character
($A-Z$), the student identifier. The next three columns have three numbers each.
The numbers are between  and , both inclusive. These numbers denote the scores
of the students in English, Mathematics, and Science, respectively.

Your task is to identify those lines that do not contain all three scores
for students.

### Input Format

There will be no more than $10$ rows of data.

Each line will be in the following format:

`[Identifier][English Score][Math Score][Science Score]`

### Output Format

For each student, if one or more of the three scores is missing, display:

`Not all scores are available for [Identifier]`

### Sample Input

```{epigraph}
A 25 27 50
B 35 75
C 75 78
D 99 88 76
```

### Sample Output

```{epigraph}
Not all scores are available for B
Not all scores are available for C
```

### Explanation

Only $2$ scores have been provided for student B and student C.

## Solution

This requires the use of the word-boundary special character (`\b`)  of regular
expressions.

```{literalinclude} /bash/sed/sed-1/sed-1.sh
:language: shell
```
