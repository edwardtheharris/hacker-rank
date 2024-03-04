#!/usr/bin/env bash

# shellcheck disable=SC2162
sort -n -k 2 -t $'\t' < /dev/stdin
