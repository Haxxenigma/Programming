#!/bin/bash
function configure_ssh_port() {
    while :; do
        if [[ $# -ne 0 ]]; then
            ssh_port=$1
            break
        fi

        read -rp "Choose which port to configure for the ssh server: " ssh_port
        if [[ ${ssh_port} -ge 0 && ${ssh_port} -le 1023 ]]; then
            echo "This port number is reserved! Select different port number"
        elif [[ ${ssh_port} -ge 1024 && ${ssh_port} -le 49151 ]]; then
            read -rp "This port number treated as semi-reserved. Continue?[y/N] " yesno
            if [[ ${yesno,,} =~ ^(y|yes)$ ]]; then
                echo "Selected: yes. Continuing..."
                break
            else
                echo "Selected: no"
            fi
        elif [[ ${ssh_port} -ge 49152 && ${ssh_port} -le 65535 ]]; then
            break
        else
            echo "Error: Invalid port number"
        fi
    done

    echo "Changing the port number to $ssh_port..."
    sed -i "s/^#*Port [0-9]*/Port $ssh_port/" "$ssh_config_file"

    echo "Opening a port on the firewall for the specified port number..."

    if command -v firewall-cmd &>/dev/null; then
        firewall-cmd --permanent --add-port $ssh_port/tcp 2>>$log_file 1>/dev/null
        handle_error "Failed to add port with firewall-cmd!"

        firewall-cmd --reload 2>>$log_file 1>/dev/null
        handle_error "Failed to reload firewalld!"
    elif command -v ufw &>/dev/null; then
        ufw allow $ssh_port/tcp 2>>$log_file 1>/dev/null
        handle_error "Failed to add port with ufw!"
    else
        echo "Warning: Firewall management tool not found!"
    fi

    if [[ -f "/etc/selinux/config" ]]; then
        echo "Configuring SELinux contents..."
        semanage port -a -t ssh_port_t -p tcp $ssh_port 2>>$log_file 1>/dev/null
        handle_error "Failed to configure SELinux contents!"
    fi

    restart_ssh
}
