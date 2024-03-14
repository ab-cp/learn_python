#!/bin/bash

for f in *jan24.csv; do
  #echo "Processing file $f"
  while IFS= read -r line; do
    if [[ $line =~ "2024-01" ]]; then
      # Use awk to format floating-point numbers
      formatted_line=$(awk -F ',' '{
          for(i=1; i<=NF; i++) {
              if ($i ~ /^[0-9]+(\.[0-9]+)?$/) {  # Check if it's a decimal number
                  printf "%.2f", $i;  # Format to two decimal places
              } else {
                  printf "%s", $i;  # Print as is if not a decimal number
              }
              printf "%s", (i<NF ? FS : RS);  # Add field separator or record separator
          }
      }' <<< "$line")
      echo "${f%%_*},$formatted_line" 
    fi
  done < "$f"
done
