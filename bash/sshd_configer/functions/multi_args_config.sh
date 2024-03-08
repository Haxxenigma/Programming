#!/bin/bash
function configure_multi_args_option() {
    declare -A option_arguments
    option="${@: -1}"

    while true; do
        echo "Choose one of this arguments:"
        for ((i = 1; i < $#; i++)); do
            option_arguments[$i]="${!i}"
            echo "[$i] ${option_arguments[$i]}"
        done
        echo "[0] Exit"
        echo ""

        read -rp "Enter: " argument

        if [[ argument -ge 1 && argument -lt $# ]]; then
            echo "Changing '$option' parameter to '${option_arguments[$argument]}'"
            sed -i "s/^#*$option [a-z|-]*/$option ${option_arguments[$argument]}/" "$ssh_config_file"
            restart_ssh
            break
        elif [[ argument -eq 0 ]]; then
            echo "Exiting..."
            exit
        else
            echo "Error: Invalid argument selected!"
        fi
    done
}
