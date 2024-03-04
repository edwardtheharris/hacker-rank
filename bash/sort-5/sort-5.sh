#!/usr/bin/env bash

# shellcheck disable=SC2162
sort -nr -k 2 -t $'\t' < /dev/stdin
