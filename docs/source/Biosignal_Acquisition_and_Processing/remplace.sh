#!/bin/bash

file=$1

#cat ${file} | sed  's/�//g'

cat ${file} | sed 's/\.\.//g'




