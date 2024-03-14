#!/bin/bash

# Function to get top 3 CPU consuming processes and their names
get_top_processes() {
    ps -e -o pid,%cpu,comm | sort -nrk 2 | awk 'NR<=3 {print $1 "," $2 "," $(NF)}' | while IFS=, read -r pid cpu process_name; do
        echo "$pid,$cpu,$(basename "$process_name")"
    done
}

# Loop 10 times to dump CPU usage of top 3 processes into CSV file
#for i in {1..10}; do
while true; do
    # Get current epoch timestamp
    timestamp=$(date +%s)

    # Get top 3 CPU consuming processes and their names
    top_processes=$(get_top_processes)

    # Append data to CSV file
    #echo "$timestamp,$top_processes" >> cpu_usage.csv
    echo "$top_processes" | while IFS= read -r process_line; do
        echo "$timestamp,$process_line"
    done
    # Wait for 1 second
    sleep 1
done
