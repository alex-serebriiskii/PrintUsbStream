#!/usr/bin/env bash

echo "Envronment Setup for Radio Serial Printing"

echo "Checking if git is installed..."
if command -v git > /dev/null 2>&1; then
  echo "Git is installed, going to next step" 
else
    echo "Git is not installed" 
    echo "Installing git..."
    sudo apt install git
fi

echo "Cloning down the script repository"
if [ ! -d "/home/$USER/RadioSerialPrinter" ]
then
    mkdir /home/$USER/RadioSerialPrinter
    pushd /home/$USER/RadioSerialPrinter
    git clone https://github.com/as4377/PrintUsbStream.git
    popd
fi

echo "Setting up the printing environment"
if command -v cups > /dev/null 2>&1; then
    echo "Cups is installed, going to next step"
else
    echo "Cups in not installed"
    echo "Installing cups..."
    sudo apt install cups
fi

echo "Configuring usermod..."
sudo usermod -a -G lpadmin $USER

echo "Setting up chromium"
if command -v chromium-browser > /dev/null 2>&1; then
    echo "Chromium is installed, going to next step"
else
    echo "Chromium is not installed"
    echo "Installing chromium..."
    sudo apt install chromium-browser
fi

echo "Please set up the printer.."
chromium-browser http://localhost:631/admin &

echo "Once printer setup is complete please execute StartPrintingService.sh"