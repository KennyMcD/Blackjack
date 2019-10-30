#!/bin/bash
echo   "Creating output.txt"
echo   "Run 1: 0 Hits"
printf "1\n2\nn" | python3 blackjack.py >> output.txt 
echo   "Run 2: 1 Hit"
printf "1\n1\n2\nn" | python3 blackjack.py >> output.txt
echo   "Run 3: 2 Hits"
printf "1\n1\n1\n2\nn" | python3 blackjack.py >> output.txt

