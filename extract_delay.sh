#!/bin/bash

BASE_DIR="."

for SCENARIO in "$BASE_DIR"/*; do
    [ -d "$SCENARIO" ] || continue

    IPERF_LOSS_OUT="$SCENARIO/iperf_loss.csv"
    IPERF_DELAY_OUT="$SCENARIO/iperf_delay.csv"
    PING_LOSS_OUT="$SCENARIO/ping_loss.csv"
    PING_DELAY_OUT="$SCENARIO/ping_delay.csv"

    > "$IPERF_LOSS_OUT"
    > "$IPERF_DELAY_OUT"
    > "$PING_LOSS_OUT"
    > "$PING_DELAY_OUT"

    for HOST_DIR in "$SCENARIO/iperf"/*; do
        [ -d "$HOST_DIR" ] || continue
        FILE="$HOST_DIR/iperf_$(basename "$HOST_DIR").csv"

        if [ -f "$FILE" ]; then
            LOSS=$(awk -F ',' '{print $(NF)}' "$FILE")
            DELAY=$(awk -F ',' '{print $(NF-1)}' "$FILE")

            echo "$LOSS" >> "$IPERF_LOSS_OUT"
            echo "$DELAY" >> "$IPERF_DELAY_OUT"
        fi
    done

    for HOST_DIR in "$SCENARIO/ping"/*; do
        [ -d "$HOST_DIR" ] || continue
        FILE="$HOST_DIR/ping_$(basename "$HOST_DIR").log"

        if [ -f "$FILE" ]; then
            LOSS=$(grep "packet loss" "$FILE" | awk '{print $(NF-4)}')
            echo "$LOSS" >> "$PING_LOSS_OUT"

            DELAY=$(grep -oP 'rtt min/avg/max/mdev = [\d\.]+/\K[\d\.]+' "$FILE")
            echo "$DELAY" >> "$PING_DELAY_OUT"
        fi
    done
done

