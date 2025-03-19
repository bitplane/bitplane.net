#!/bin/bash

pause() {
    stty -echo  # Disable echo
    stty raw    # Enable raw mode (captures key press immediately)
    read -n1    # Wait for a single key press
    stty -raw   # Disable raw mode
    stty echo   # Re-enable echo
}

cd src

clear
cat 1.1*.ans
pause

clear
cat 1.2*.ans
pause

clear
cat 1.3*.ans
pause

clear
cat 1.4*.ans
pause

speed=10

./type.sh 8 3 $speed "Tyler gets me a job as a wai"
./type.sh 8 4 $speed "ter, after that Tyler's stuf"
./type.sh 8 5 $speed "fing a gun in my mouth and s"
./type.sh 8 6 $speed "aying the first step to eter"
./type.sh 8 7 $speed "al life is you have to die. "
pause


