#!/bin/bash

read -r divisor
array=($(cat))
array=${array[*]}

printf %.3f $(echo $((${array// /+}))/$divisor | bc -l)