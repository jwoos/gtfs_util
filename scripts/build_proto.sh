#! /usr/bin/env sh

wget --output-document=src/gtfs/realtime.proto \
	https://developers.google.com/transit/gtfs-realtime/gtfs-realtime.proto

protoc -I=src/gtfs --python_out=src/gtfs src/gtfs/realtime.proto
