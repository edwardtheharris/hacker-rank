#!/usr/bin/env bash

# shellcheck disable=SC2162
awk '{
        if ((getline tmp) > 0) {
            print $0";"tmp
        } else { print $0";" }
    }' -
