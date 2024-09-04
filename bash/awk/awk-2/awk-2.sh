#!/usr/bin/env bash

# shellcheck disable=SC2162
awk '{ sum = $2 + $3 + $4; avg = sum / 3; if (avg > 49) {print $1" : Pass"}; if (avg < 50) {print $1" : Fail"} }' -
