#! /usr/bin/env sh


if [[ "$1" == 'run' ]]; then
	docker run \
		-it \
		--rm \
		-v $(pwd):/opt \
		python_mta:latest bash
elif [[ "$1" == 'build' ]]; then
	docker build . \
		--tag python_mta:latest
else
	echo 'Invalid command - try run or build'
	exit 1
fi
