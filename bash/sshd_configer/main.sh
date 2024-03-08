#!/bin/bash
source_files=$(ls ./functions)
ssh_config_file="/etc/ssh/sshd_config"
log_file="./errors.log"
ssh_port=22

if [[ ! -f $log_file ]]; then
    touch $log_file
fi

for file in ${source_files}; do
    source ./functions/$file
done

if [[ ! -f "$ssh_config_file" ]]; then
    echo "Error: Can not find sshd config file!"
    exit
elif [[ ! -f $ssh_config_file.bak ]]; then
    echo "Creating a backup copy of the current sshd configuration file..."
    cp "$ssh_config_file" "$ssh_config_file.bak"
fi

if ! systemctl --quiet is-active sshd; then
    echo "The SSH service is not active. Activating..."
    systemctl enable --now sshd
    handle_error "Unable to enable ssh service!"
fi

if [[ $# -ne 0 && $1 =~ ^[0-9]+$ ]]; then
    configure_ssh_port $1
elif [[ $# -ne 0 && $1 =~ ^(-h|--help|help)$ ]]; then
    echo "TIP: You can pass any number as the first argument \
to the script to configure the sshd port number with that number"
    exit
fi

while true; do
    echo "Select options to configure:"
    echo "[1] SSH port number"
    echo "[2] Maximum authentication tries"
    echo "[3] Maximum sessions"
    echo "[4] Permit root login to ssh"
    echo "[5] Public key authentication"
    echo "[6] Password authentication"
    echo "[7] Restore defaults from backup file"
    echo "[0] Exit"
    echo ""

    read -rp "Enter: " option

    if [[ -z $option ]]; then
        echo -e "Error: No option selected!\n"
    elif [[ option -eq 0 ]]; then
        echo -e "Exiting...\n"
        exit
    elif [[ option -eq 1 ]]; then
        configure_ssh_port
    elif [[ option -eq 2 ]]; then
        configure_number_option "Enter number of maximum authentication tries: " "MaxAuthTries"
    elif [[ option -eq 3 ]]; then
        configure_number_option "Enter number of maximum sessions: " "MaxSessions"
    elif [[ option -eq 4 ]]; then
        arguments=(yes prohibit-password without-password forced-commands-only no)
        configure_multi_args_option "${arguments[@]}" "PermitRootLogin"
    elif [[ option -eq 5 ]]; then
        arguments=(yes no)
        configure_multi_args_option "${arguments[@]}" "PubkeyAuthentication"
    elif [[ option -eq 6 ]]; then
        arguments=(yes no)
        configure_multi_args_option "${arguments[@]}" "PasswordAuthentication"
    elif [[ option -eq 7 ]]; then
        echo "Restoring defaults from a backup file..."
        cp "$ssh_config_file.bak" "$ssh_config_file"
        restart_ssh
    else
        echo -e "Error: Invalid option selected\n"
    fi
done
