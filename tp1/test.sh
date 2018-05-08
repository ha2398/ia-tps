#!/bin/bash

# Script to run the search algoritms and gather data.

NUM_POINTS=$1
MAP=$2

POINTS=$(python3 ./source/PointGen.py $NUM_POINTS)

rm -rf test_outputs
mkdir test_outputs

mkdir test_outputs/AStarM
mkdir test_outputs/AStarO
mkdir test_outputs/UniformCost
mkdir test_outputs/BestFirst
mkdir test_outputs/IDS

touch test_outputs/log.txt
echo -e "Points used:\n" >> test_outputs/log.txt

IFS=" " read -ra COORDS <<< "$POINTS"

COUNTER=0
INDEX=0
IX=0
IY=0
FX=0
FY=0
while [ $COUNTER -lt $NUM_POINTS ]; do
	echo "Ponto $((COUNTER+1))"
	let INDEX=COUNTER*4

	let IX=${COORDS[$((INDEX))]}
	echo -n "${COORDS[$((INDEX))]} " >> test_outputs/log.txt

	let IY=${COORDS[$((INDEX+1))]}
	echo -n "${COORDS[$((INDEX+1))]} " >> test_outputs/log.txt

	let FX=${COORDS[$((INDEX+2))]}
	echo -n "${COORDS[$((INDEX+2))]} " >> test_outputs/log.txt

	let FY=${COORDS[$((INDEX+3))]}
	echo -n "${COORDS[$((INDEX+3))]} " >> test_outputs/log.txt

	mkdir test_outputs/AStarM/$((COUNTER+1))
	mkdir test_outputs/AStarO/$((COUNTER+1))
	mkdir test_outputs/UniformCost/$((COUNTER+1))
	mkdir test_outputs/BestFirst/$((COUNTER+1))
	mkdir test_outputs/IDS/$((COUNTER+1))

	echo "A* Manhattan"
	./source/tp1.py $MAP $IX $IY $FX $FY astar -d -he 1 > test_outputs/AStarM/$((COUNTER+1))/output.txt

	echo "A* Octile"
	./source/tp1.py $MAP $IX $IY $FX $FY astar -d -he 2 > test_outputs/AStarO/$((COUNTER+1))/output.txt

	echo "Uniform Cost"
	./source/tp1.py $MAP $IX $IY $FX $FY uc -d > test_outputs/UniformCost/$((COUNTER+1))/output.txt

	echo "Best First"
	./source/tp1.py $MAP $IX $IY $FX $FY bf -d > test_outputs/BestFirst/$((COUNTER+1))/output.txt

	echo "IDS"
	./source/tp1.py $MAP $IX $IY $FX $FY ids -d > test_outputs/IDS/$((COUNTER+1))/output.txt

	echo -e "" >> test_outputs/log.txt

	let COUNTER=COUNTER+1
done

