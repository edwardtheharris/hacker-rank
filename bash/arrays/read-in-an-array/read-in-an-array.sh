#!/usr/bin/env bash

# shellcheck disable=SC2162
while read array_line; do
    country_array+=("${array_line}")
done

for country in "${country_array[@]}"; do
    printf "%s " "${country}"
done
