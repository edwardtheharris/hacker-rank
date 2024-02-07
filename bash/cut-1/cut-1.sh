#!/bin/bash

# Specify the file path
input_file="/dev/stdin"
# Set n to 3 to extract the 3rd character
n=3

# Read each line from the file
while IFS= read -r line
do
  # Extract the 3rd character from the line
  # Bash indexing starts at 0, but we use n-1 here because we're extracting based on user expectation (1-based indexing)
  echo "${line:n-1:1}"
done < "$input_file"
