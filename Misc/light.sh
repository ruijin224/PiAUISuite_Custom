#!/bin/bash

aplay -c 1 -t wav -r 44100 -f cd /home/pi/PiAUISuite_Custom/Misc/clap.wav
sleep 1
aplay -c 1 -t wav -r 44100 -f cd /home/pi/PiAUISuite_Custom/Misc/clap.wav
sleep 0.2
aplay -c 1 -t wav -r 44100 -f cd /home/pi/PiAUISuite_Custom/Misc/clap.wav

