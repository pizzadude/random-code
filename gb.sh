#!/bin/bash
# Frontend for GNUboy
# Requires GNUboy
# Put this script in your GB/GBC rom dir
# Then type the full name of the file...
# ...you want to run.
clear
echo "Gameboy Rom Selector"
echo "--------------------"
echo "Select a game"
echo " "
ls
read romfile
sdlgnuboy --scale=3 --fullscreen=0 "$romfile"
