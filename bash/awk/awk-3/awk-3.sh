#!/usr/bin/env bash

# shellcheck disable=SC2162
awk '{ sum = $2 + $3 + $4; avg = sum / 3; if (avg < 50) {print $1" "$2" "$3" "$4" : FAIL"}; if (avg > 50 && avg < 60) {print $1" "$2" "$3" "$4" : C"}; if (avg > 60 && avg < 80) {print $1" "$2" "$3" "$4" : B"}; if (avg > 80) {print $1" "$2" "$3" "$4" : A"} }' -
