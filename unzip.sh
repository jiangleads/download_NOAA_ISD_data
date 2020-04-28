#! /bin/bash
iyear=$1
year1=$2
if [ ! -n "$iyear" ] ; then
			iyear=1901
fi

if [ ! -n "$year1" ] ; then
			year1=2019
fi

while  [ ${iyear} -le ${year1} ]; do
				echo "$iyear : "$line $line2
				cd $iyear
				echo "$PWD"
				"ls *.gz|xargs gzip -d"
				cd ..
			let iyear++
done

