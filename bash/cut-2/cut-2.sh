#!/bin/bash

while read -r line; do
  printf "%s\n" "${line:1:1}${line:6:1}"
done
