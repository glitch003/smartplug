#!/bin/sh
echo "Content-Type: text/plain"
echo "Cache-Control: no-cache, must-revalidate"
echo "Expires: Sat, 26 Jul 1997 05:00:00 GMT"
echo

RELAY_CTRL=/sys/class/leds/tp-link:blue:relay/brightness

CURRENT_STATE="`cat $RELAY_CTRL`"

NEW_STATE=$(($CURRENT_STATE - 1))
NEW_STATE=$(($NEW_STATE * -1))     

echo $NEW_STATE > $RELAY_CTRL
