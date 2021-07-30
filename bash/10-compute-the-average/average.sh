#!/bin/bash

divisor=0
sum=0

while IFS= read -r line || [[ -n "$line" ]];
do
    if [[ $divisor == 0 ]]
    then
        divisor=$line
    else
        sum=$(bc -s <<< "${sum} + ${line}")
    fi
done

average=$(bc -s <<< "scale=3; ${sum} / ${divisor}")

printf "${average}"