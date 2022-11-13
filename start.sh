#!/bin/bash
python controler.py
touch index.html
echo '<table style="border: 1px solid black;"><tr style="border: 1px solid black;">' > index.html
while read x
do
echo "<td style='border: 1px solid black;'>$x</td>" >> index.html
done < 'in/in.txt'
echo "</tr>" >> index.html
while read y
do
echo "<td style='border: 1px solid black;'>$y</td>" >> index.html
done < 'out/out.txt'
echo "</tr></table>" >>index.html
