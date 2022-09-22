#!/bin/bash
# prints the content-length of a url to stdout
curl -sI "$1" | grep -i content-length | cut -d ":" -f2
