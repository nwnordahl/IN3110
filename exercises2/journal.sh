#!/bin/bash

function journal {
# A simple journal
    if [ "$1" == "log" ]; then
        cut -c9-11 journal.txt | uniq -c
    else
        MESSAGE="$(date +'%Y-%m-%d %H:%M:%S') - $1"
        echo $MESSAGE 1>> journal.txt
    fi
}
