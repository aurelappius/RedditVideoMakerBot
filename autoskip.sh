#!/bin/bash

# Run the program with unbuffered output
stdbuf -oL python3 main.py | while read -r line; do
    if [[ "$line" == "Do you want to skip the post? (y/n)" ]]; then
        echo "y"   # Answer 'y' to skip the post
    elif [[ "$line" == "Do you want the error traceback for debugging purposes? (y/n)" ]]; then
        echo "n"   # Answer 'n' to skip the error traceback
    else
        echo "$line"   # Print any other output
    fi
done