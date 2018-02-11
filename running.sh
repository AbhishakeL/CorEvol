#!/bin/env bash

###########
### This is the first portion which maps the file names according to the file name of the inserted files and loci and count
###########



########
#### Checks if the out folder if already present. If present then deletes the folder.
#### Needs to to check if we need to check for symlinks.
########


if [ -d "seq_out" ]; then
	rm -R seq_out
fi


rm -f genome_list.txt
rm -f seq.fasta
rm -f ref_cds.list
rm -f ref_pro.list
mkdir seq_out

cd ./sequences
if ls *.gz&>/dev/null; then
	gunzip -q *.gz
else
	echo "Files are already unzipped"
fi


#for f in ./sequences/*.gbff
for f in *
do
	#r=$(grep "DBLINK      BioProject:" $f| head -n 1|cut -d ":" -f 2|cut --complement -c 1)
	mkdir ../seq_out/$f
	#chname=$(echo $f|cut -d "/" -f 3)
	#echo $chname $'\t' $r >> genome_list.txt
	echo $f >> ../genome_list.txt

	csplit --digit=3 --quiet --elide-empty-files --prefix=$f. $f "/^///+1" "{*}"
	#mv ./$r.* ./seq_out/$r/
	mv ./$f.* ../seq_out/$f/
	rename 's/$/.gbk/' ../seq_out/$f/*
	#### this is where the python file to split the gbff comes in.####
done
cd ../seq_out

for f in *
do
	python ../dummy.py $f
	find . -type f -empty -delete
	cat $f/*.cds > $f/$f.merged
	cat $f/*.pro > $f/$f.promerged
done


###This is input file for cd-hit###
find . -type f -name "*.merged" -exec cat {} \; > ../seq.fasta
### This is the reference cds file ###
find . -type f -name "*.refcds" -exec cat {} \; > ../ref_cds.list
### This is the reference  protein file ###
find . -type f -name "*.promerged" -exec cat {} \; > ../ref_pro.list
