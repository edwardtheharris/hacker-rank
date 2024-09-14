#!/bin/bash
# shellcheck disable=SC2001,SC2086

# Initialize the grid size
rows=63
cols=100

# Create an empty grid filled with underscores
grid=()
for ((i = 0; i < rows; i++)); do
  grid[i]=$(printf '%*s' $cols '' | tr ' ' '_')
done

# Function to draw the Y-shape recursively
draw_fractal() {
  local r=$1    # Starting row
  local c=$2    # Starting column (center of the Y)
  local size=$3 # Size of the Y (length of each branch)
  local iter=$4 # Remaining iterations

  # Draw the vertical part of the Y
  for ((i = 0; i < size; i++)); do
    tc=$c
    grid[r-i]=$(echo "${grid[r-i]}" | sed "s/./1/$tc")
    tc=$((tc+1))
  done

  # Draw the two diagonal branches of the Y
  for ((i = 1; i <= size; i++)); do
    ltc=$c
    rtc=$c
    grid[r-size-i+1]=$(echo "${grid[r-size-i+1]}" | sed "s/./1/$((ltc - i))")
    grid[r-size-i+1]=$(echo "${grid[r-size-i+1]}" | sed "s/./1/$((rtc + i))")
    ltc=$((ltc - i + 1))
    rtc=$((rtc + i + 1))
  done

  # If iterations remain, draw smaller Y-shapes recursively
  if (( iter > 1 )); then
    draw_fractal $((r - 2 * size)) $((c - size)) $((size / 2)) $((iter - 1))
    draw_fractal $((r - 2 * size)) $((c + size)) $((size / 2)) $((iter - 1))
  fi
}

# Read the number of iterations
read -r iterations

# Start drawing the fractal tree
initial_size=16
start_row=$((rows - 1))
start_col=$((cols / 2))

# Call the recursive function with the initial parameters
draw_fractal $start_row $start_col $initial_size $iterations

# Print the grid row by row
for ((i = 0; i < rows; i++)); do
  echo "${grid[i]}"
done

