#!/bin/bash

s1=$1
s2=$2
file=$3

sed -i "s/$s1/$s2/g" "$file"


