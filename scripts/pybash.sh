#!/bin/bash

list_sndfiles=()


# (find `pwd` | grep ".wav") | {
(find `pwd` -regex ".*/.*\.\(wav\|mp3\)") | {
	while read line; 
	do 
		list_sndfiles+=("$line ##")
	done

	#echo ${list_sndfiles[@]}	
	#echo ${#list_sndfiles[@]}

	python script_generate_profile.py ${list_sndfiles[@]}
}