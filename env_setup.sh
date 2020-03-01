#!/usr/bin/env bash

echo "Envronment Setup for Radio Serial Printing"

echo "Installing git..."
sudo apt install git

echo "Cloning down the script repository"
if [ ! -d "/home/$USER/RadioSerialPrinter" ]
then
    mkdir /home/$USER/RadioSerialPrinter
    pushd /home/$USER/RadioSerialPrinter
    git clone https://github.com/as4377/PrintUsbStream.git
    popd
fi

echo "Setting up the printing environment"
sudo apt install cups
sudo usermod -a -G lpadmin $USER

chromium-browser http://localhost:631/admin &

echo "Once printer setup is complete please execute StartPrintingService.sh"