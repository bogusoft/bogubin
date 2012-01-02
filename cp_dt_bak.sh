#!/bin/bash

# cp_dt_bak.sh
#
# Make a backup copy of a file with the current date and time and a
# .bak extension appended to the file name.
#
# 2012-01-02 (bill@melvin.org)

if [ $# -lt 1 ]; then
  echo
  echo "Usage: $0 filename"
  exit 1
fi

filename=$1

dt=`date +%Y%m%d_%H%M%S`

copyname="${filename}.${dt}.bak"

echo "Copy: ${filename}"
echo "  to: ${copyname}"

cp $filename $copyname
