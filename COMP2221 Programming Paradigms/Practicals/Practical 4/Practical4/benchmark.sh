#!/bin/bash

PROGRAMS=("./vector_array" "./vector_pointer")

INPUT_SIZES=(1000 1000000 1000000000 1000000000000)

ITERATIONS=1000

for PROGRAM in "${PROGRAMS[@]}"; do
    echo "Testing runtimes for $PROGRAM"
    for SIZE in "${INPUT_SIZES[@]}"; do

        total_time=0

        for ((i=1; i<=ITERATIONS; i++)); do
            t=$({ time $PROGRAM; } 2>&1 | grep "real" | tr -d "sreal\t" | sed 's/0m//g')

            total_time=$(echo "$total_time + $t" | bc)
        done

        average=$(echo "scale=6; $total_time / $ITERATIONS" | bc)
        echo "Average time for size $SIZE: 0$average seconds"
    done
    echo ""
done