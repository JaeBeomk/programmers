#!/bin/bash
# 사용법 csv.sh [읽을 파일] [저장할]
READ=$1
SAVE=$2

echo "_id,data" > $SAVE



COUNTER=1

while read LINE; do

        echo "$COUNTER,$LINE" >> $SAVE

        COUNTER=$(($COUNTER+1))

done < $1 

