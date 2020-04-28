#!/bin/bash

while read line
do
    year=${line: -7:-3}
    fname=${line::-3}
    filepath="/shares/Public2/NOAA/"$year"/"$line
    fpath="/shares/Public2/NOAA/"$year"/"$fname
    if [ -f "$filepath" ];then
       echo $filepath "exist"
    else
        if [ -f "$fpath" ];then
            echo $fpath" exist"
        else
            cmd="curl -s ftp.ncdc.noaa.gov/pub/data/noaa/"$year"/"$line" -o /shares/Public2/NOAA/"$year"/"$line
            $cmd
 #           echo "cmd"
 #           echo $cmd
 #           echo "fname"
 #           echo $fname
 #           echo "filepath"
 #           echo $filepath
 #           echo "fpath"
 #           echo $fpath
        fi
    fi
done < filelist.txt
