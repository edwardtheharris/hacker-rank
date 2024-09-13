#!/bin/bash
# shellcheck disable=SC2162

while read country; do
    countries+=("$country")
done

for country in "${countries[@]}"; do
    echo "$country" | grep -v -e '[aA]' > /dev/stdout || true
done
