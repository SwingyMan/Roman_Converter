#!/bin/bash
set -x
set -e
date=$(date "+%Y-%m-%d-%H:%M:%S")
cd in
count=$(ls -1q *|wc -l)
cd ..
if [[ -e raport.html ]]; then
    cp raport.html "backup/$date.html"
    else
      touch raport.html
fi
cd in
for ((i=1;i<=$count;i++)) ; do
    :
    input=$(cat $i.txt)
    cd ..
    result=$(python3 main.py $input)
    cd out
    echo $result > "$i.txt"
    cd ..
    cd in
done
cd ..
python3 generate.py