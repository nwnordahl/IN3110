#!/bin/bash

function track {
# Track tasks.

    if [ -f "track.txt" ]; then
        if [ "$(tail -n1 'track.txt' | cut -d' ' -f1)" == "LABEL" ]; then
            START="on"
        else
            START="off"
        fi
    else
        START="off"
    fi

    if [ "$1" == "start" ]; then
        if [ $START == "off" ]; then
            START="on"
            NAME=$2
            echo "START $(date)" >> track.txt
            echo "LABEL $NAME" >> track.txt
        else
            echo "There is already a task being tracked"
        fi
    elif [ "$1" == "stop" ]; then
        if [ $START == "on" ]; then
            START="off"
            echo "END $(date)" >> track.txt
            echo >> track.txt
        else
            echo "There is no task currently being tracked"
        fi
    elif [ "$1" == "status" ]; then
        if [ $START == "on" ]; then
            echo "Currently tracking ${NAME}."
        else
            echo "There is no active task"
        fi
    else
	cat <<-EOF
	Usage: track <command>
	Commands:
	start <label> - Start tracking a new task with name <label>
	stop - Stop tracking task
	status - Show current status of tracking
	EOF
    fi
}
