#!/bin/bash
while true
do 
	clear;
	echo -------------Current submitted MARCC jobs-----------;
	sqme; 
	echo -------------Current team\'s MARCC balance----------; 
	sbalance; 
	echo -------------$1 Content \(tail\)--------; 
	tail $1; 
	echo -------------Number of "readings"-------------------;
	cat $1 | grep reading | wc -l;
	echo -------------Number of "writings"-------------------; 
	cat $1 | grep writing | wc -l; 
	echo --------------$2 Content \(tail\)-------; 
	tail $2;  
	sleep 200; 
done
