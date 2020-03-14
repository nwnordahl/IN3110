#!/bin/bash

function climb {
# Go back directories

    declare -i n; n=0

    if [ $# -eq 0 ]; then
        cd ..
    else
        if [ 0 -gt $1 ]; then
            echo "Argument must be a positive integer."
        else
            while [ $1 -gt $n ]; do
                cd ..
                ((n++))
            done
        fi
    fi
}
