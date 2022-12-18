#!/bin/bash
date=$(date "+%Y-%m-%d-%H:%M:%S")
while choice=$(dialog --title "Kalendarz Rzymski" --menu "Wybierz opcję" 12 45 25 1 "Uruchom skrypt" 2 "Stwórz Backup" 3 "O autorze" 4 "Wyjdz" 2>&1 >/dev/tty)
  do
  case $choice in
      1) cd in
          count=$(ls -1q *|wc -l)
          cd ..
          rm *.html
          touch "$date.html"
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
          python3 generate.py "$date.html"
          dialog --title "Gotowe" --msgbox "Zadanie wykonane!" 6 20;;
      2) mkdir backup/$date
          mv *.html "backup/$date/"
          cp -R in backup/$date/
          cp -R out backup/$date/
          dialog --title "Gotowe" --msgbox "Zadanie wykonane!" 6 20;;
      3)  dialog --title "Gotowe" --msgbox "Projekt stworzony przez Marcina Bogus w językach Python i Bash.
Celem programu miała być dwustronna zamiana systemów cyfr rzymskich i arabskich." 12 80;;
      *) exit;;
  esac
done
