#!/bin/bash

BASE_DIR="."

PING_JITTER_10="dados/ping_jitter/ping_jitter_10.csv"
PING_JITTER_15="dados/ping_jitter/ping_jitter_15.csv"
PING_JITTER_20="dados/ping_jitter/ping_jitter_20.csv"

> "$PING_JITTER_10"
> "$PING_JITTER_15"
> "$PING_JITTER_20"

for SCENARIO in "$BASE_DIR"/*; do
    [ -d "$SCENARIO" ] || continue

    if [[ "$SCENARIO" == *"host10"* ]]; then
        OUTPUT_FILE="$PING_JITTER_10"
    elif [[ "$SCENARIO" == *"host15"* ]]; then
        OUTPUT_FILE="$PING_JITTER_15"
    elif [[ "$SCENARIO" == *"host20"* ]]; then
        OUTPUT_FILE="$PING_JITTER_20"
    else
        continue
    fi

    JITTER_FILE="$SCENARIO/ping_jitter.csv"

    if [ -f "$JITTER_FILE" ]; then
        cat "$JITTER_FILE" >> "$OUTPUT_FILE"
    fi
done

