#!/usr/bin/env bash
# prints the content-length of a url to stdout
curl --no-progress-meter --head "$1" | grep -i content-length | cut -d ":" -f2
