#!/bin/bash

zipcode=`cat $HOME/.misc | awk -F'zipcode==' '{print $2}'`
result=`python /home/pi/PiAUISuite_Custom/Misc/getweather.py "$zipcode"`

echo "$result"
tts "$result"

