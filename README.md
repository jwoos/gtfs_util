# GTFS Parser

## What?
This is a library to work with GTFS data.

~This is a Python library to provide access to MTA's API. It will try to accommodate your needs by doing as little or as much work you want it to do.~

The general high level functionality is as follows:

- Fetch static data from the MTA's site
  - Cache it for the configured length of time
  - Parse the feeds into objects with relations
  - Get specific data, instead of bundles
- Fetch real time data from the MTA's site
  - Cache it for the configured length of time
  - Parse GTFS real time into JSON
  - Relate the real time data back to the static data

## Why?

The MTA's API is all over the place - their real time bus API has its own site and sign up process, completely separate from the subway real time bus API. Their documentation is all over the place as well choosing to kick it back to Google who defined GTFS - but that still leaves extensions and optional parameters to be figured out.
