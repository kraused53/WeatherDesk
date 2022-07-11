#!/bin/bash

# These two lines look for the Ubuntu desktop environment and exports a refference to it
# This gives the python program the context needed to be able to run when called from CRON
PID=$(pgrep -t tty2 gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

/usr/bin/python3 /home/daniel/Documents/projects/WeatherDesk/WeatherDesk/main.py