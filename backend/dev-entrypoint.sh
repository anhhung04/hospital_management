#!/bin/sh
echo 'Starting migration...'
alembic upgrade head

while true; do
    python3 -m debugpy --listen 0.0.0.0:8888 app.py
    echo 'App crashed, restarting in 5 seconds...'
    sleep 5
done