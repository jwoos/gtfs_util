#!/usr/bin/env bash

virtualenv /tmp/gtfs_parser-ve
source /tmp/gtfs_parser-ve/bin/activate


./$1
