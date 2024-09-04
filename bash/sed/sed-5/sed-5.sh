#!/usr/bin/env bash

# shellcheck disable=SC2162
sed -e 's/\([0-9]\{4\}\) \([0-9]\{4\}\) \([0-9]\{4\}\) \([0-9]\{4\}\)/\4 \3 \2 \1/' -
