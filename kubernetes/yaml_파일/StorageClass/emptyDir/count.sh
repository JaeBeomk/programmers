#! /bin/bash

trap "exit" SIGINT
mkdir /var/htdocs

SET=$(seq 0 99999)

for i in $SET

do 
    echo "Running Loop seq" $i > /var/htdocs/index.html

done
