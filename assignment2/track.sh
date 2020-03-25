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
    elif [ "$1" == "log" ]; then
        declare -i n; n=1
        if [ "$(tail -n1 track.txt | cut -d' ' -f1)" == "LABEL" ]; then
            while read t; do
                if [ $n -eq $(($(wc -l track.txt | cut -d' ' -f1) - 2)) ]; then
                    break
                fi

                if [ $((n % 4)) -eq 1 ]; then
                    LOG_START=$(echo $t | cut -d' ' -f2-)
                    LOG_START=$(date --date '$LOG_START' +%s) # Date converted to seconds since the UNIX epoch
                elif [ $((n % 4)) -eq 2 ]; then
                    LOG_NAME=$(echo $t | cut -d' ' -f2-)
                elif [ $((n % 4)) -eq 3 ]; then
                    LOG_STOP=$(echo $t | cut -d' ' -f2-)
                    LOG_STOP=$(date --date '$LOG_STOP' +%s) # Date converted to seconds the UNIX epcoch
                    LOG_TOTAL=$((LOG_START -LOG_STOP))
                    echo ${LOG_NAME}: $LOG_TOTAL
                fi 
                ((n++))
            done < track.txt
        else
            while read t; do
                if [ $((n % 4)) -eq 1 ]; then
                    LOG_START=$(echo $t | cut -d' ' -f2-)
                    LOG_START=$(date --date '$LOG_START' +%s) # Date converted to seconds since the UNIX epoch
                elif [ $((n % 4)) -eq 2 ]; then
                    LOG_NAME=$(echo $t | cut -d' ' -f2-)
                elif [ $((n % 4)) -eq 3 ]; then
                    LOG_STOP=$(echo $t | cut -d' ' -f2-)
                    LOG_STOP=$(date --date '$LOG_STOP' +%s) # Date converted to seconds since the UNIX epoch
                    LOG_TOTAL=$((LOG_START - LOG_STOP))
                    echo ${LOG_NAME}: $LOG_TOTAL
                fi
                ((n++))
            done < track.txt
        fi
    else
	cat <<-EOF # -EOF for printing indented lines
	Usage: track <command>
	Commands:
	start <label> - Start tracking a new task with name <label>
	stop - Stop tracking task
	status - Show current status of tracking
	log - Show time usage of tasks
	EOF
    fi
}
