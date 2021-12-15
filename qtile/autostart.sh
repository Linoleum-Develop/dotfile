#!/bin/sh

#Screen Resolution
xrandr --output VGA-0 --off --output HDMI-0 --off --output eDP --primary --mode 1366x768 --pos 0x0 --rotate normal 

#set keyboard
setxkbmap la-latin1 &

#system icons

picom &

volumeicon &

nm-applet &

udiskie -t &

cbatticon -u 5 &

nitrogen --restore &

lxappeaance --restore &
