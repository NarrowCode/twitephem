#!/bin/bash

WEEKS=0
DAYS=0
YEARS=0

# Get arguments
while getopts w:d:y: option
do
case "${option}"
in
w) WEEKS=${OPTARG};;
d) DAYS=${OPTARG};;
y) YEARS=${OPTARG};;
esac
done

BEGINDATE="01-01-1990"

# Check OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then 
    CURRENTDATE=`date +"%d-%m-%Y %H:%M"`
    DT=`date`
    ENDDATE=$(date --date="${DT} -${DAYS} days -${WEEKS} weeks -${YEARS} years" +%d-%m-%Y) 

elif [[ "$OSTYPE" == "darwin"* ]]; then
    CURRENTDATE=`gdate +"%d-%m-%Y %H:%M"`
    DT=`gdate`
    ENDDATE=$(gdate --date="${DT} -${DAYS} days -${WEEKS} weeks -${YEARS} years" +%d-%m-%Y) 
else
    echo OS not supported. Aborting.
fi

echo $CURRENTDATE
echo "  - BEG:  ${BEGINDATE}"
echo "  - END:  ${ENDDATE}"

echo "  - CALL:" twitephem.py -a -s -b $BEGINDATE -e $ENDDATE
python twitephem.py -a -s -b $BEGINDATE -e $ENDDATE
