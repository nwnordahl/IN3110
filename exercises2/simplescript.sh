#!/bin/bash

NAME=$1
AGE=$2

CHAR=$(expr $(echo $1 | wc -m) - $(echo $1 | wc -w))
WORD=$(echo $1 | wc -w)

if [ $WORD -gt 1 ]; then
    echo "Your name is $NAME, and it consists of $CHAR letters and $WORD words"
else
    echo "Your name is $NAME, and it's only one word consisting of $CHAR letters"
fi

echo "Your age is $AGE"

VAL=$(expr $AGE + 10)

if [ $VAL -gt 59 ]; then
    echo "Wow, you're old!"
fi
