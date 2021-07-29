#!/bin/bash

divisor=0
input=input/input00.txt
sum=0

while read -r line;
do
    if [[ $divisor == 0 ]];
    then
        divisor=$line
    else
        sum=$((sum + line))
    fi
done < $input

printf "${sum}"