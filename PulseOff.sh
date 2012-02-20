#!/bin/bash

cd /usr/bin
gksudo "chmod -x pulseaudio"
killall pulseaudio
