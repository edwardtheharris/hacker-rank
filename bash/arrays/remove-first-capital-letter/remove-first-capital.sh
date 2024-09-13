#!/bin/bash
# shellcheck disable=SC2162

while read country; do
    countries+=("$country")
done

for country in "${countries[@]}"; do
    printf "%s " "${country/[A-Z]/.}"
done
