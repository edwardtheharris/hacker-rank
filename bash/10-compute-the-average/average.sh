#!/bin/bash

read -r divisor
array=("$(cat)")
array_string=${array[*]}

printf "%.3f" "$(echo $((${array_string// /+}))/$divisor | bc -l)"
