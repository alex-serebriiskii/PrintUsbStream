#!/usr/bin/env bash

echo "Launching The Printing Service"

if [ -d "/home/$USER/RadioSerialPrinter" ]
then
    pushd /home/$USER/RadioSerialPrinter/PrintUsbStream
    chmod +x serial_reader.py
    ./serial_reader.py
    popd
else
    echo "Failed to detect proper service setup, please run env_setup.sh"
fi