#! /bin/bash
echo "统计下载的各年的文件数目:"
iyear=$1
year1=$2
if [ ! -n "$iyear" ] ; then
			iyear=1902
fi

if [ ! -n "$year1" ] ; then
			year1=2019
fi

while  [ ${iyear} -le ${year1} ]; do
				line=$(find ./$iyear/* -name "*$iyear*" |wc -l)
				line2=$(cat filelist.txt|grep $iyear.gz |wc -l)
				if [ "$line" -ne  "$line2" ]; then
				echo "$iyear : "$line $line2
				else 
				echo "$iyear: True"
				fi
		let iyear++
done

