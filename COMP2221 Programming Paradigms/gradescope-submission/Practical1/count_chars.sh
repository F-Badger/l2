#!/bin/bash
for file in *;
do
    if [ -f "$file" ]; then
        char_count=$(wc -m < "$file")
        echo "The number of characters in the file $file: $char_count"
    fi
done
