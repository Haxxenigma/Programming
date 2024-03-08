#!/bin/bash
function handle_error() {
    if [[ $? -ne 0 ]]; then
        echo "Error: $1"
        echo "Restoring previous configuration..."
        cp $ssh_config_file.bak $ssh_config_file
        systemctl restart sshd 2>>$log_file
        exit
    fi
}

function restart_ssh() {
    echo "Restarting sshd service..."
    systemctl restart sshd 2>>$log_file
    handle_error "Failed to restart sshd service!"
    echo -e "Success!\n"
    sleep 1
}
