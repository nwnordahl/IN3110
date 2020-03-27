#!/bin/bash

function wc {
    if [ $# -eq 0 ]; then
        echo You have to provide a filename
        echo You can also use '*' and '*.py'
    elif [ $# -gt 1 ]; then
        echo Only provide one argument
    else   
        ./wc.py "$1"
    fi
}
