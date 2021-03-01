#!/usr/bin/env bash
declare -i i=1
while
    sleep 2
    echo "intento: $i"
    (( i++ ))
    orator migrate --config config.py --force 2>> errout.log
(( $? != 0 ));do :;done
python fainews.py
