#!/bin/sh
source .venv/bin/activate
while true; do
    nordvpn connect
    sleep 2
    python3 main.py
    sleep 2
    nordvpn disconnect
    sleep 2
done