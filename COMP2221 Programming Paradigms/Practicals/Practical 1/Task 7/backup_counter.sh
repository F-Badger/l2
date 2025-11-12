#!/usr/bin/bash
X=0
Y=0
for file in "$1"/*;
do
	if [[ "$file" == *.conf || "$file" == *.log ]]
	then
		((X++))
		((Y += $(wc -c < "$file")))
	fi
done
touch backup_summmary.txt
> backup_summary.txt
echo "TOTAL_FILES: $X" >> backup_summary.txt
echo "TOTAL_SIZE: $Y" >> backup_summary.txt
DATE=$(date "+%Y-%m-%d %H:%M:%S")
echo "SCAN_COMPLETED: '$DATE'" >> backup_summary.txt
