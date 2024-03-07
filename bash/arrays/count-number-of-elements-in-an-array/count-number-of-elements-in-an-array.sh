#!/usr/bin/env bash

# shellcheck disable=SC2162
while read array_line; do
    country_array+=("${array_line}")
done

printf "%s" "${#country_array[@]}"
