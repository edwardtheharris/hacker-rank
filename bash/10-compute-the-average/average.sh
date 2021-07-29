#!/bin/bash

count=0
input=input/input00.txt
sum=0

while read -r line;
do
    if [[ $count == 0 ]];
    then
        divisor=$line
    else
        
    fi
done < $input