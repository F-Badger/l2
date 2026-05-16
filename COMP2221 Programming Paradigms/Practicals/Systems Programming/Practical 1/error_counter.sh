#!/usr/bin/bash
DATA=$(sed '1d' "$1")
OCURRENCE_COUNTS=$(echo "$DATA" | grep -oE "^[1-3]" | sort | uniq -c)
X=$(echo "$OCURRENCE_COUNTS" | sed -n '1p'| sed 's/^ *//' | grep -oE "^[0-9]*")
Y=$(echo "$OCURRENCE_COUNTS" | sed -n '2p'| sed 's/^ *//' | grep -oE "^[0-9]*")
Z=$(echo "$OCURRENCE_COUNTS" | sed -n '3p'| sed 's/^ *//' | grep -oE "^[0-9]*")
TOP_ISSUE=$(echo "$DATA" | grep -oE "ERROR|INFO|WARNING" | sort | uniq -c | sort -r | head -n1 | tr -cd "A-Z")
LINES=$(echo "$DATA" | wc -l)
DATE=$(date "+%Y-%m-%d")

touch error_analysis.txt
> error_analysis.txt
echo "CRITICAL: $X" >> error_analysis.txt
echo "WARNING: $Y" >> error_analysis.txt
echo "INFO: $Z" >> error_analysis.txt
echo "MOST_COMMON_ISSUE: $TOP_ISSUE" >> error_analysis.txt
echo "TOTAL_ENTRIES: $LINES" >> error_analysis.txt
echo "ANALYSIS_DATE: $DATE" >> error_analysis.txt
