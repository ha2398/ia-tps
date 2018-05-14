#!/bin/bash

# Script to run the search algoritms and gather data.


MAP=$1
IX=$2
IY=$3
FX=$4
FY=$5

IFS="/" read -ra MAPS <<< "$MAP"
IFS="." read -ra MAPS <<< "${MAPS[1]}"
folder="${MAPS[0]}-$IX-$IY-$FX-$FY"

rm -rf tests/$folder
mkdir tests/$folder

echo "A* Manhattan"
./source/tp1.py $MAP $IX $IY $FX $FY astar -d -he 1 > tests/$folder/astar1.log

echo "A* Octile"
./source/tp1.py $MAP $IX $IY $FX $FY astar -d -he 2 > tests/$folder/astar2.log

echo "Uniform Cost"
./source/tp1.py $MAP $IX $IY $FX $FY uc -d > tests/$folder/ucs.log

echo "Best First"
./source/tp1.py $MAP $IX $IY $FX $FY bf -d > tests/$folder/bf.log

#echo "IDS"
#./source/tp1.py $MAP $IX $IY $FX $FY ids -d > tests/$folder/ids.log
