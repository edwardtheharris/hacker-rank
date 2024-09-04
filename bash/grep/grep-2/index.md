---
abstract: >-
    grep prints lines that contain a match for one or more patterns.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-02-07
title: grep command 1
---

[![grep #2](https://img.shields.io/badge/grep_%232-hackerrank?style=flat&logo=hackerrank&label=HackerRank)](https://www.hackerrank.com/challenges/text-processing-in-linux-the-grep-command-2/problem?isFullScreen=true)

## Objective

In this challenge, we practice using the grep command to find specified strings or regular expressions.

### Resources

{term}`grep` is a multi-purpose search tool that is used to find specified
strings or regular expressions. A variety of options exist that makes it
possible to use this command in several different ways and to handle many
different situations. For example, one might opt for a case-insensitive search,
or to display only the fragment matching the specified search pattern. The
command could also be used to display only the line number of an input file
where the specified string or regular expression has been found.

Before using {term}`grep`, we recommend becoming familiar with regular
expressions to be able to harness the command to its fullest.

More details about common examples of grep usage can be found
[here](http://tldp.org/LDP/abs/html/textproc.html).

- [15 Practical Grep Command Examples](http://www.thegeekstuff.com/2009/03/15-practical-unix-grep-command-examples/)
- [TLDP Examples for Grep](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_02.html)

## Task

You are given a text file that will be piped into your command through `STDIN`.
Use grep to display all those lines that contain the word the in them.
The search should NOT be sensitive to case.
Display only those lines of the input file that contain the word 'the'.

### Input Format

A text file will be piped into your command through `STDIN`.

### Output Format

Output only those lines that contain the word 'the'. The search should NOT be
case sensitive. The relative ordering of the lines in the output should be the
same as it was in the input.

### Sample Input

```{epigraph}
From fairest creatures we desire increase,
That thereby beauty's rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,
Making a famine where abundance lies,
Thy self thy foe, to thy sweet self too cruel:
Thou that art now the world's fresh ornament,
And only herald to the gaudy spring,
Within thine own bud buriest thy content,
And tender churl mak'st waste in niggarding:
Pity the world, or else this glutton be,
To eat the world's due, by the grave and thee.
When forty winters shall besiege thy brow,
And dig deep trenches in thy beauty's field,
Thy youth's proud livery so gazed on now,
Will be a tattered weed of small worth held:
Then being asked, where all thy beauty lies,
Where all the treasure of thy lusty days;
To say within thine own deep sunken eyes,
Were an all-eating shame, and thriftless praise.
How much more praise deserved thy beauty's use,
If thou couldst answer 'This fair child of mine
Shall sum my count, and make my old excuse'
```

### Sample Output

```{epigraph}
But as the riper should by time decease,
Thou that art now the world's fresh ornament,
And only herald to the gaudy spring,
Pity the world, or else this glutton be,
To eat the world's due, by the grave and thee.
Where all the treasure of thy lusty days;
```

### Explanation

We have retained only those lines which contain the word 'the'. Do remember,
that in this problem we're trying to make a case insensitive search. This means
that your command should also be able to capture 'The', 'thE' and so on. A
little bit of extra care might be required to avoid retaining cases where 'the'
is a suffix or prefix of some other word within the sentences!

## Solution

The key to this solution is to add the `-i` (case insensitive) and `-w`
(match only instances surrounded by word boundaries) flags to the command.

```{literalinclude} /bash/grep/grep-2/grep-2.sh
```

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>
```
