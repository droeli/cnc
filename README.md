# CNC (can not click)

## What
Program to click for you after you did not move your mouse for some seconds

## Config
Amount of time (seconds) before a click is done is default 1s
config.ini (ex: none_move_wait=2.5) overrides default
Command line argument -w overrides config.ini

## Get started

pip install -r requirements.txt 

## Build:

pyinstaller -F cnc.py

-> cnc.exe is in dist dir