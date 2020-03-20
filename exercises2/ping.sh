#!/bin/bash

timeout 0.2 ping -c1 google.com &> /dev/null

if [ "$?" == "0" ]; then
    echo "The internet is working"
else
    echo "The internet is not working"
fi
