#!/bin/bash

BASE_DIR="."

PING_DELAY_10="dados/ping_delay/ping_delay_10.csv"
PING_DELAY_15="dados/ping_delay/ping_delay_15.csv"
PING_DELAY_20="dados/ping_delay/ping_delay_20.csv"

> "$PING_DELAY_10"
> "$PING_DELAY_15"
> "$PING_DELAY_20"

for SCENARIO in "$BASE_DIR"/*; do
    [ -d "$SCENARIO" ] || continue

    if [[ "$SCENARIO" == *"host10"* ]]; then
        OUTPUT_FILE="$PING_DELAY_10"
    elif [[ "$SCENARIO" == *"host15"* ]]; then
        OUTPUT_FILE="$PING_DELAY_15"
    elif [[ "$SCENARIO" == *"host20"* ]]; then
        OUTPUT_FILE="$PING_DELAY_20"
    else
        continue
    fi

    DELAY_FILE="$SCENARIO/ping_delay.csv"

    if [ -f "$DELAY_FILE" ]; then
        cat "$DELAY_FILE" >> "$OUTPUT_FILE"
    fi
done

