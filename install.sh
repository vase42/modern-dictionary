#!/bin/bash

echo "Installing Modern Dictionary CLI..."

# Ensure Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Please install Python3 and try again."
    exit 1
fi

# Ensure script is running in the correct directory
if [[ ! -f "modern-dictionary.py" ]]; then
    echo "Error: modern-dictionary.py not found! Please run this script from the correct directory."
    exit 1
fi

# Install dependencies
if [[ -f "requirements.txt" ]]; then
    pip install -r requirements.txt
else
    echo "Warning: requirements.txt not found. Skipping dependency installation."
fi

# Move script to /usr/local/bin and make it executable
chmod +x modern-dictionary.py
sudo mv modern-dictionary.py /usr/local/bin/modern-dictionary

RED='\033[0;31m'
WHITE='\033[1;37m'
NC='\033[0m'

echo -e "${RED}///////////////////////${NC}"
echo -e "${RED}// ${WHITE}Modern Dictionary${WHITE}${RED} //${NC}"
echo -e "${RED}///////////////////////${NC}"
echo "Installation complete! Run 'modern-dictionary [WORD]' or 'modern-dictionary -r' for a random definition."
