#!/bin/bash

divisor=0
sum=0
average=0.0

while read -r line;
do
    if [[ $divisor == 0 ]];
    then
        divisor=$line
    else
        sum=$((sum + line))
    fi
done

average=$((sum / divisor))

printf "${average}"