#!/bin/bash

read -p "What's Your Name? " name
echo "Your name: ${name}; and it's size: ${#name}"

array=()

for ((i = 0; i < 10; i++)); do
    array[$i]=$RANDOM
done

echo -e "\nArray: ${array[@]}"
read -p "Choose, how many items from array you want to extract: " selection

if [[ $selection -eq 1 ]]; then
    read -p "Choose position: " index
    echo "${array[index - 1]}"
else
    read -p "Choose where to start: " start
    echo "${array[@]:$start-1:$selection}"
fi