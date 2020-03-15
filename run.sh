#!/bin/bash
sh /var/scripts/access_log_update
python3 /var/scripts/coordinates
python3 /var/scripts/locator
python /var/scripts/map.py
python3 /var/scripts/dynindex "Welcome to flexonmyex.de"
python3 /var/scripts/dynaccesslog
