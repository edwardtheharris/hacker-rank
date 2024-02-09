#!/bin/bash

while read line; do
  printf "%s\n" "${line:1:1}${line:6:1}"
done
