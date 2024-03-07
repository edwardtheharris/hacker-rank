---
abstract: The middle of a text file problem from HackerRank.
authors: Xander Harris
title: Middle of a Text File
---

[![Middle of a Text File | HackerRank](https://img.shields.io/badge/Middle%20of%20a%20Text%20File-green?style=for-the-badge&logo=hackerrank&label=HackerRank)](https://www.hackerrank.com/challenges/text-processing-in-linux---the-middle-of-a-text-file/)

## Problem

Display the lines (from line number $12$ to $22$, both inclusive) of a given text file.

### Input Format

A text file

### Output Format

Display the lines (from line number $12$ to $22$, both inclusive) for the input file.

### Sample Input

```{card} Sample Input
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

```{card} Sample Output
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
```

## Solution

```{literalinclude} middle-of-a-text-file.sh
:language: shell
:caption: middle-of-a-text-file.sh
```

```{index} text; slice of a text file
```
