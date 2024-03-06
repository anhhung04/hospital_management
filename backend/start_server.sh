#!/bin/sh
if [ $DEBUG = "1" ]
then
    echo "Running in debug mode"
    uvicorn app:app --reload --host 0.0.0.0 --port 8000
else
# Start the server
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
fi