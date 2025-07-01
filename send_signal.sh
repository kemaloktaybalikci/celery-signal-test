#!/bin/bash

PID=$(ps aux | grep 'celery -A celery_signal_test worker' | grep -v grep | awk '{print $2}')
SIGNAL=$1

if [ -z "$PID" ]; then
  echo "Celery worker not running."
  exit 1
fi

if [ -z "$SIGNAL" ]; then
  echo "Usage: $0 <SIGINT|SIGTERM|SIGKILL>"
  exit 1
fi

echo "Sending $SIGNAL to PID $PID"
kill -s $SIGNAL $PID
