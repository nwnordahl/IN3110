#!/bin/bash

timeout 0.2 ping -c 1 google.com &> /dev/null

echo $?


