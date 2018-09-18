#! /usr/bin/env sh


PATH_PREFIX='data/static'

mkdir -p $PATH_PREFIX data/realtime

# stations
wget --output-document=$PATH_PREFIX/subway_stations.csv \
	http://web.mta.info/developers/data/nyct/subway/Stations.csv

# subway schedule
wget --output-document=$PATH_PREFIX/subways.zip \
	http://web.mta.info/developers/data/nyct/subway/google_transit.zip

mkdir -p $PATH_PREFIX/subway
unzip -d $PATH_PREFIX/subway $PATH_PREFIX/subways.zip

# bus - bronx
wget --output-document=$PATH_PREFIX/bus_bronx.zip \
	http://web.mta.info/developers/data/nyct/bus/google_transit_bronx.zip

mkdir -p $PATH_PREFIX/bus/bronx
unzip -d $PATH_PREFIX/bus/bronx $PATH_PREFIX/bus_bronx.zip

# bus - brooklyn
wget --output-document=$PATH_PREFIX/bus_brooklyn.zip \
	http://web.mta.info/developers/data/nyct/bus/google_transit_brooklyn.zip

mkdir -p $PATH_PREFIX/bus/brooklyn
unzip -d $PATH_PREFIX/bus/brooklyn $PATH_PREFIX/bus_brooklyn.zip

# bus - manhattan
wget --output-document=$PATH_PREFIX/bus_manhattan.zip \
	http://web.mta.info/developers/data/nyct/bus/google_transit_manhattan.zip

mkdir -p $PATH_PREFIX/bus/manhattan
unzip -d $PATH_PREFIX/bus/manhattan $PATH_PREFIX/bus_manhattan.zip

# bus - queens
wget --output-document=$PATH_PREFIX/bus_queens.zip \
	http://web.mta.info/developers/data/nyct/bus/google_transit_queens.zip

mkdir -p $PATH_PREFIX/bus/queens
unzip -d $PATH_PREFIX/bus/queens $PATH_PREFIX/bus_queens.zip

# bus - staten island
wget --output-document=$PATH_PREFIX/bus_staten_island.zip \
	http://web.mta.info/developers/data/nyct/bus/google_transit_staten_island.zip

mkdir -p $PATH_PREFIX/bus/staten_island
unzip -d $PATH_PREFIX/bus/staten_island $PATH_PREFIX/bus_staten_island.zip

# TODO LIRR
# TODO MetroNorth
