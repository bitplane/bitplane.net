#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 x y ms \"text\""
    exit 1
fi

x=$1
y=$2
ms=$3
text=$4

# Save the current cursor position and terminal colors
tput sc

# Move the cursor to the specified position
tput cup "$y" "$x"
echo -en "\e[0m\e[38;2;0;0;0m\e[48;2;255;255;255m"

# Type the text letter by letter
for ((i = 0; i < ${#text}; i++)); do
    echo -n "${text:$i:1}"
    sleep "$(awk "BEGIN {print $ms / 1000}")"
done

# Reset colors and restore cursor position
tput sgr0
tput rc
