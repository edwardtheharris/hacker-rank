---
abstract: >-
    sed is a popular utility which enables
    quick parsing and transformation of text.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-02-07
title: Sed command 1
---

[![sed #1](https://img.shields.io/badge/sed_%231-hackerrank?style=flat&logo=hackerrank&label=HackerRank)](https://www.hackerrank.com/challenges/text-processing-in-linux-the-sed-command-1/problem?isFullScreen=true)

## Objective

[In this challenge](https://www.hackerrank.com/challenges/text-processing-in-linux-the-sed-command-1/problem?isFullScreen=true),
we will practice using the sed command to parse and transform
text.

## Resources

{term}`sed` is a popular tool that enables quick parsing and transformation of
text.

### Examples of {term}`sed` in action

Substitute the first occurrence of 'editor' with 'tool':

```{code-block} shell
echo "My favorite programming editor is Emacs. Another editor I like is Vim." | sed -e s/editor/tool/

# ---
# My favorite programming tool is Emacs. Another editor I like is Vim.
```

Substitute all the occurrences of 'editor' with 'tool':

```{code-block} shell
echo "My favorite programming editor is Emacs. Another editor I like is Vim." | sed -e s/editor/tool/g

# ---
# My favorite programming tool is Emacs. Another tool I like is Vim.
```

Substitute the second occurrence of 'editor' with 'tool':

```{code-block} shell
echo "My favorite programming editor is Emacs. Another editor I like is Vim." | sed -e s/editor/tool/2

# ---
# My favorite programming editor is Emacs. Another tool I like is Vim.
```

Highlight all the occurrences of 'editor' by wrapping them up in brace brackets:

```{code-block} shell
echo "My favorite programming editor is Emacs. Another editor I like is Vim." | sed -e s/editor/{\&}/g

# ---
# My favorite programming {editor} is Emacs. Another {editor} I like is Vim.
```

The following links are useful to learn about sed:

- [Sed - An Introduction and a tutorial](http://www.grymoire.com/Unix/Sed.html#uh-10a)
- [The TLDP Guide](http://tldp.org/LDP/abs/html/x23170.html)
- [Some Practical Examples](http://www.folkstalk.com/2012/01/sed-command-in-unix-examples.html)

## Task

For each line in a given input file, transform the first occurrence of the
word 'the' with 'this'. The search and transformation should be strictly case
sensitive.

### Input Format

A text file will be piped into your command through STDIN.

### Output Format

Transform the text as specified by the task.

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
From fairest creatures we desire increase,
That thereby beauty's rose might never die,
But as this riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,
Making a famine where abundance lies,
Thy self thy foe, to thy sweet self too cruel:
Thou that art now this world's fresh ornament,
And only herald to this gaudy spring,
Within thine own bud buriest thy content,
And tender churl mak'st waste in niggarding:
Pity this world, or else this glutton be,
To eat this world's due, by the grave and thee.
When forty winters shall besiege thy brow,
And dig deep trenches in thy beauty's field,
Thy youth's proud livery so gazed on now,
Will be a tattered weed of small worth held:
Then being asked, where all thy beauty lies,
Where all this treasure of thy lusty days;
To say within thine own deep sunken eyes,
Were an all-eating shame, and thriftless praise.
How much more praise deserved thy beauty's use,
If thou couldst answer 'This fair child of mine
Shall sum my count, and make my old excuse'
```

### Explanation

The line:

```{epigraph}
"But as the riper should by time decease,"
```

has been transformed to:

```{epigraph}
"But as this riper should by time decease,"
```

The line:

```{epigraph}
"To eat the world's due, by the grave and thee."
```

has been transformed to:

```{epigraph}
"To eat this world's due, by the grave and thee."
```

## Solution

This requires the use of the word-boundary special character (`\b`)  of regular
expressions.

```{literalinclude} /bash/sed/sed-1/sed-1.sh
:language: shell
```
