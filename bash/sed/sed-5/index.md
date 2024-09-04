---
abstract: >-
    sed is a popular utility which enables
    quick parsing and transformation of text.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-09-04
title: Sed command 5
---

[![sed #5](https://img.shields.io/badge/sed_%235-hackerrank?style=flat&logo=hackerrank&label=HackerRank)](https://www.hackerrank.com/challenges/sed-command-5/problem?isFullScreen=true)

## Overview

{term}`sed` is a popular utility which enables quick parsing and transformation
of text.

Here are some very simple examples of {term}`sed` in action.

### Examples

Substitute the first occurrence of 'editor' with 'tool'.

```{code-block} shell
echo "My favorite programming editor is Emacs. Another editor I like is Vim." | sed -e s/editor/tool/

# ---
# My favorite programming tool is Emacs. Another editor I like is Vim.
```

Substitute all the occurrences of 'editor' with 'tool'.

```{code-block} shell
echo "My favorite programming editor is Emacs. Another editor I like is Vim." | sed -e s/editor/tool/g

# ---
# My favorite programming tool is Emacs. Another tool I like is Vim.
```

Substitute the second occurrence of 'editor' with 'tool'.

```{code-block} shell
echo "My favorite programming editor is Emacs. Another editor I like is Vim." | sed -e s/editor/tool/2

# ---
# My favorite programming editor is Emacs. Another tool I like is Vim.
```

Highlight all the occurrences of 'editor' by wrapping them up in brace brackets.

```{code-block} shell
echo "My favorite programming editor is Emacs. Another editor I like is Vim." | sed -e s/editor/{\&}/g

# ---
# My favorite programming {editor} is Emacs. Another {editor} I like is Vim.
```

### References

Some references for learning about sed have been included:

- [Sed - An Introduction and a tutorial](http://www.grymoire.com/Unix/Sed.html#uh-10a)
- [The TLDP Guide](http://tldp.org/LDP/abs/html/x23170.html)
- [Some Practical Examples](http://www.folkstalk.com/2012/01/sed-command-in-unix-examples.html)

## Task

Given an input file, with $N$ credit card numbers, each in a new line, your task
is to reverse the ordering of segments in each credit card number. Assume that
the credit card numbers will have 4 space separated segments with 4 digits each.

If the original credit card number is `1434 5678 9101 1234`,
transform it to `1234 9101 5678 1434`.

```{admonition} Useful References:
This particular [page on StackOverflow](http://stackoverflow.com/questions/2232200/regular-expression-in-sed-for-masking-credit-card)
has a relevant example about sed, groups
and back references. [Here](http://www.thegeekstuff.com/2009/10/unix-sed-tutorial-advanced-sed-substitution-examples/)'s
a detailed tutorial covering groups and
back references.
```

### Input Format

$N$ credit card numbers, each in a new line, credit card numbers will have 4
space separated segments with 4 digits each.

### Constraints

However, the value of $N$ does not matter while writing your command.

### Output Format

$N$ lines, each containing a credit card number with the ordering of its
segments reversed.

### Sample Input

```{epigraph}
1234 5678 9101 1234
2999 5178 9101 2234
9999 5628 9201 1232
8888 3678 9101 1232
```

### Sample Output

```{epigraph}
1234 9101 5678 1234
2234 9101 5178 2999
1232 9201 5628 9999
1232 9101 3678 8888
```

### Explanation

The order of the four segments in the (input) credit card numbers have been
reversed.

## Solution

This problem is solved easily with some groups and back references.

```{literalinclude} /bash/sed/sed-5/sed-5.sh
:l
