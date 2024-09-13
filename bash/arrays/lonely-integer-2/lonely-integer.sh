#!/bin/bash
# shellcheck disable=SC2162,SC2034

# Read number of integers
read n

# Read array of integers
read -a int_array

# Init result for XOR
result=0
for i in "${int_array[@]}"; do
    result=$(("$result" ^ "$i"))
done

echo "$result"

