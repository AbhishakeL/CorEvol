#!/bin/sh

###########
### This is the first portion which maps the file names to the BioProject ID.
###########



########
#### Checks if the out folder if already present. If present then deletes the folder.
#### Needs to to check if we need to check for symlinks.
########


if [ -d "seq_out" ]; then
	rm -R seq_out
fi


rm -f genome_list.txt
mkdir seq_out

for f in ./sequences/*.gbff
do
	r=$(grep "DBLINK      BioProject:" $f| head -n 1|cut -d ":" -f 2|cut --complement -c 1)
	mkdir seq_out/$r
	chname=$(echo $f|cut -d "/" -f 3)
	echo $chname $'\t' $r >> genome_list.txt

	csplit --digit=2 --quiet --elide-empty-files --prefix=$r. $f "/^///+1" "{*}"
	mv ./$r.* ./seq_out/$r/
	rename 's/$/.gbk/' ./seq_out/$r/*
	#### this is where the python file to split the gbff comes in.####
done
