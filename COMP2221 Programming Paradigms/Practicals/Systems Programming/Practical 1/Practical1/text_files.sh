#!/bin/bash
DIR="./MyTextFiles"
if [ $1 == 1 ]
then
	if [ -d "$DIR" ]
	then
		:
	else
		mkdir MyTextFiles
	fi
	for file in *
	do
		filename=$(echo "$file" | tr 'A-Z' 'a-z')
		if [[ -f "$file" &&  "$filename" == *.txt ]]
		then
			cp "$file" "$DIR"/
		fi
	done
else
	if [ -d "$DIR" ]
	then
		for file in "$DIR"/*
		do
			cp "$file"  ./
		done
	else
		echo "Warning: no backup to restore from"
	fi
fi
touch "DirectoryListing.txt"
> "DirectoryListing.txt"
for file in * 
do 
	echo "$file" >> "DirectoryListing.txt"
done
wc -l < "DirectoryListing.txt"
