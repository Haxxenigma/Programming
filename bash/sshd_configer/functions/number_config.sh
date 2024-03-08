#!/bin/bash
function configure_number_option() {
    prompt="$1"
    option="$2"

    while true; do
        read -rp "$prompt" number

        if [[ ${number} =~ ^[0-9]+$ ]]; then
            echo "Changing '$option' parameter to '$number'"
            sed -i "s/^#*$option [0-9]*/$option $number/" "$ssh_config_file"
            restart_ssh
            break
        else
            echo "Error: Invalid number specified!"
        fi
    done
}
