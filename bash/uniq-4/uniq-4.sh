#!/usr/bin/env bash

# shellcheck disable=SC2162
uniq -ci < /dev/stdin | awk '{$1=$1};1'
