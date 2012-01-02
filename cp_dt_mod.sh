#!/bin/bash

# cp_dt_mod.sh
#
# Make a copy of a file with the files's modification time added to
# the file name and preserving the extension.
#
# 2012-01-02 (bill@melvin.org)

if [ $# -lt 1 ]; then
  echo
  echo "Usage: $0 filename"
  exit 1
fi

filename=$1
name=${filename%.*}
ext=${filename##*.}

modtime=`stat -c %y ${filename}`

# Output from stat:
#....:....1....:....2....:....3....:
#2011-12-27 23:22:48.837939230 -0500

suffix="${modtime:0:4}${modtime:5:2}${modtime:8:2}_${modtime:11:2}${modtime:14:2}${modtime:17:2}"

copyname="${name}.${suffix}.${ext}"

echo "Copy: ${filename}"
echo "  to: ${copyname}"

cp $filename $copyname
