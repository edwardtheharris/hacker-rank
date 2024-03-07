#!/usr/bin/env bash

declare -a country_array

# shellcheck disable=SC2162
while IFS= read -r array_line || [[ -n "$array_line" ]]; do
    country_array+=("${array_line}")
done

country_array+=("${country_array[@]}" "${country_array[@]}")

printf "%s " "${country_array[@]}"
