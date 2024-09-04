#!/usr/bin/env bash

# shellcheck disable=SC2162
awk 'NF != 4 { printf("Not all scores are available for %s\n", $1) }' -
