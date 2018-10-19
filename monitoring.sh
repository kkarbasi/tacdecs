#!/bin/bash
while true
do 
	clear;
	echo -------------MARCC Job Monitoring-------------------;
	sqme; 
	printf "%*s\n" $(tput cols) '' | tr ' ' -
	echo -------------Current team\'s MARCC balance----------; 
	sbalance; 
	printf "%*s\n" $(tput cols) '' | tr ' ' -
	echo -------------$1 Content \(tail\)--------; 
	tail $1;
	printf "%*s\n" $(tput cols) '' | tr ' ' -
	echo -------------$2 Content \(tail\)--------;
	tail $2 
	printf "%*s\n" $(tput cols) '' | tr ' ' -
	echo -------------Number of "readings"-------------------;
	cat $1 | grep reading | wc -l;
	printf "%*s\n" $(tput cols) '' | tr ' ' -
	echo -------------Number of "writings"-------------------; 
	cat $1 | grep writing | wc -l; 
	printf "%*s\n" $(tput cols) '' | tr ' ' -
	find ../scratch/auto_processed -type f -name "*.pkl" | wc -l
	sleep 30; 
done
