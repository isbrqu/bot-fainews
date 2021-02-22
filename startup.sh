#!/usr/bin/env bash
while
    sleep 2
    orator migrate --config orator_config.py --force 2> /dev/null
(( $? != 0 ));do :;done
python fainews.py
