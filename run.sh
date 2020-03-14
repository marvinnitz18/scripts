#!/bin/bash
sh /var/scripts/access_log_update
python3 /var/scripts/coordinates
python3 /var/scripts/locator
python3 /var/scripts/map.py
