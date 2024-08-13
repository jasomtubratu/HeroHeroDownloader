#!/bin/bash

if [ -f /etc/os-release ]; then
    . /etc/os-release
    if [[ $ID == "ubuntu" ]]; then
        sudo apt update
        sudo apt install ffmpeg -y
    elif [[ $ID == "centos" ]]; then
        sudo yum update
        sudo yum install ffmpeg -y
    elif [[ $ID == "fedora" ]]; then
        sudo dnf update
        sudo dnf install ffmpeg -y
    else
        echo "Unsupported distribution: $ID"
        exit 1
    fi
else
    echo "Unable to determine distribution"
    exit 1
fi