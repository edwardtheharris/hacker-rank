#!/usr/bin/env bash

# shellcheck disable=SC2162
uniq -c < /dev/stdin | awk '{$1=$1};1'
