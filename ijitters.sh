#!/bin/bash

BASE_DIR="."

IPERF_JITTER_10="dados/iperf_jitter/iperf_jitter_10.csv"
IPERF_JITTER_15="dados/iperf_jitter/iperf_jitter_15.csv"
IPERF_JITTER_20="dados/iperf_jitter/iperf_jitter_20.csv"

> "$IPERF_JITTER_10"
> "$IPERF_JITTER_15"
> "$IPERF_JITTER_20"

for SCENARIO in "$BASE_DIR"/*; do
    [ -d "$SCENARIO" ] || continue

    if [[ "$SCENARIO" == *"host10"* ]]; then
        OUTPUT_FILE="$IPERF_JITTER_10"
    elif [[ "$SCENARIO" == *"host15"* ]]; then
        OUTPUT_FILE="$IPERF_JITTER_15"
    elif [[ "$SCENARIO" == *"host20"* ]]; then
        OUTPUT_FILE="$IPERF_JITTER_20"
    else
        continue
    fi

    IPERF_LOG="$SCENARIO/iperf_server.log"

    if [ -f "$IPERF_LOG" ]; then
        grep "Mbits/sec" "$IPERF_LOG" | awk '{print $9}' >> "$OUTPUT_FILE"
    fi
done

