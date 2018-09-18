#! /usr/bin/env sh

wget --directory-prefix=gtfs https://developers.google.com/transit/gtfs-realtime/gtfs-realtime.proto

protoc -I=gtfs --python_out=gtfs gtfs/gtfs-realtime.proto
