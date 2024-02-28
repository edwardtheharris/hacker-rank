#!/usr/bin/env bash

# shellcheck disable=SC2162
while read line_txt; do
    echo "${line_txt}" | cut -c -4
done
