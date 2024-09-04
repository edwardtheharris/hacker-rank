---
abstract: >-
    sed is a popular utility which enables
    quick parsing and transformation of text.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-02-07
title: Sed command 2
---

[![sed #2](https://img.shields.io/badge/sed_%232-hackerrank?style=flat&logo=hackerrank&label=HackerRank)](https://www.hackerrank.com/challenges/text-processing-in-linux-the-sed-command-2/problem?isFullScreen=true)

## Objective

In this challenge, we will practice using the sed command to parse and transform text.

## Resources

[Sed](http://en.wikipedia.org/wiki/Sed) is a popular tool that enables quick parsing and transformation of text.

Examples of sed in action:

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

For each line in a given input file, transform all the occurrences of the word
'thy' with 'your'. The search should be case insensitive, i.e. 'thy', 'Thy',
'tHy' etc. should be transformed to 'your'.

## Input Format

A text file will be piped into your command via STDIN.

## Output Format

Transform and display the text as required in the task.

## Sample Input

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

## Sample Output

```{epigraph}
From fairest creatures we desire increase,
That thereby beauty's rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st your light's flame with self-substantial fuel,
Making a famine where abundance lies,
your self your foe, to your sweet self too cruel:
Thou that art now the world's fresh ornament,
And only herald to the gaudy spring,
Within thine own bud buriest your content,
And tender churl mak'st waste in niggarding:
Pity the world, or else this glutton be,
To eat the world's due, by the grave and thee.
When forty winters shall besiege your brow,
And dig deep trenches in your beauty's field,
your youth's proud livery so gazed on now,
Will be a tattered weed of small worth held:
Then being asked, where all your beauty lies,
Where all the treasure of your lusty days;
To say within thine own deep sunken eyes,
Were an all-eating shame, and thriftless praise.
How much more praise deserved your beauty's use,
If thou couldst answer 'This fair child of mine
Shall sum my count, and make my old excuse'
```

## Explanation

The line:

```{epigraph}
"Feed'st thy light's flame with self-substantial fuel,"
```

has been transformed to:

```{epigraph}
"Feed'st your light's flame with self-substantial fuel,"
```

The line:

```{epigraph}
"Thy self thy foe, to thy sweet self too cruel:"
```

has been transformed to:

```{epigraph}
"your self your foe, to your sweet self too cruel:"
```
