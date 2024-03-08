#!/bin/bash

read -p "Enter some input: " input

if [[ $input =~ ^[A-Z] ]]; then
    echo "Your input starts with uppercase letter"
else
    echo "Your input starts with lowercase letter"
fi

# Function: find_index
# Description: Finds given element's index in given array
# Parameters:
#   $1 - Array
#   $2 - Element to find
# Returns:
#   0 if element found in given array, else 1
find_index() {
    local array=("${!1}")
    local target=$2

    for ((i = 0; i < ${#array[@]}; i++)); do
        if [[ "${array[i]}" == "$target" ]]; then
            echo $i
            return 0
        fi
    done

    return 1
}

array=(0 10 25 40 60 85 115 200 350 650 1500)

echo -e "\nArray=(${array[@]})"
read -p "Choose one element from array: " choice

index=$(find_index array[@] "$choice")
exit_status=$?

if [[ $exit_status -eq 0 ]]; then
    echo -e "\nHere is your element: ${array[index]}"
    echo "And it's index in the array: $index"
else
    echo -e "\nError: Your choice $choice doesn't exist in my array"
fi