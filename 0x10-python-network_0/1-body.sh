#!/bin/bash
# prints the body of a response with status code 200
status_code=$(curl -so /dev/null -w "%{http_code}" "$1")
if [[ $status_code == "200" ]];then curl "$1"; fi
