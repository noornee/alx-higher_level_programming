#!/bin/bash
# prints the body of a response with status code 200
status=$(curl -s --head "$1" | grep "HTTP" | cut -d " " -f2)
if [[ $status == "200" ]];then curl "$1"; fi
