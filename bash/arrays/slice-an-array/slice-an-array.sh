#!/usr/bin/env bash

declare -a country_array

# shellcheck disable=SC2162
while IFS= read -r array_line || [[ -n "$array_line" ]]; do
    country_array+=("${array_line}")
done

for i in 3 4 5 6 7; do
    printf "%s " "${country_array[$i]}"
done
