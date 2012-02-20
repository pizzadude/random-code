#!/bin/bash
# frontend for festival
# requires festival
while [[ 1 ]]; do
echo "Say something:"
read say
echo "$say" |festival --tts
killall festival
clear
done
