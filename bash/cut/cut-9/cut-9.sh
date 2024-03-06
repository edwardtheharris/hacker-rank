#!/usr/bin/env bash

# shellcheck disable=SC2162
while read line_txt; do
    echo "${line_txt}" | cut -f 2-
done
