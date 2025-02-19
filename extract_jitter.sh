#!/bin/bash

BASE_DIR="."

for SCENARIO in "$BASE_DIR"/*; do
    [ -d "$SCENARIO" ] || continue

    IPERF_LOSS_OUT="$SCENARIO/iperf_loss.csv"
    IPERF_JITTER_OUT="$SCENARIO/iperf_jitter.csv"
    PING_LOSS_OUT="$SCENARIO/ping_loss.csv"
    PING_JITTER_OUT="$SCENARIO/ping_jitter.csv"

    > "$IPERF_LOSS_OUT"
    > "$IPERF_JITTER_OUT"
    > "$PING_LOSS_OUT"
    > "$PING_JITTER_OUT"

    for HOST_DIR in "$SCENARIO/iperf"/*; do
        [ -d "$HOST_DIR" ] || continue
        FILE="$HOST_DIR/iperf_$(basename "$HOST_DIR").csv"

        if [ -f "$FILE" ]; then
            LOSS=$(awk -F ',' '{print $(NF)}' "$FILE")
            JITTER=$(awk -F ',' '{print $(NF-1)}' "$FILE")
            echo "$LOSS" >> "$IPERF_LOSS_OUT"
            echo "$JITTER" >> "$IPERF_JITTER_OUT"
        fi
    done

    for HOST_DIR in "$SCENARIO/ping"/*; do
        [ -d "$HOST_DIR" ] || continue
        FILE="$HOST_DIR/ping_$(basename "$HOST_DIR").log"

        if [ -f "$FILE" ]; then
            LOSS=$(grep "packet loss" "$FILE" | awk '{print $(NF-4)}')
            echo "$LOSS" >> "$PING_LOSS_OUT"

            JITTER=$(grep "rtt min/avg/max/mdev" "$FILE" | awk -F'/' '{print $NF}' | awk '{print $1}')
            echo "$JITTER" >> "$PING_JITTER_OUT"
        fi
    done
done

