#!/bin/bash

# Start the database
echo -n "Starting the database ... "
docker run -p 5432:5432 \
           -v ${PWD}/data:/docker-entrypoint-initdb.d \
           -e POSTGRES_PASSWORD=dbpass \
           -e POSTGRES_USER=dbuser \
           -e POSTGRES_DB=nidc \
           -d \
           postgres:alpine 2>&1 > /dev/null
echo "Done."