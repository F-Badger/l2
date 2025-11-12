#!/bin/bash
touch processed_logs.csv
echo "Priority,Type,Date,Time,Issue,Value,Server" > processed_logs.csv
cat "$1" | tr "#*@" "1-3" | tr "|" "," | sort -t, -k4 >> processed_logs.csv
