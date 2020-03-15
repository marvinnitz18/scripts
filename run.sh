#!/bin/bash
sh access_log_update
python3 coordinates
python3 locator
python map.py
python3 dynindex "Welcome to flexonmyex.de"
python3 dynaccesslog
