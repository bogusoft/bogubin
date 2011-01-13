#!/usr/bin/env python

# bmp2jpg.py 
# 2011-01-13 bill@melvin.org

import os, Image

print 'Converting BMP to JPG in ' + os.getcwd()
for f in os.listdir(os.getcwd()):
    name, ext = os.path.splitext(f)
    if ext.lower() == ".bmp":
        outfile = name + ".jpg"
        print '  ' + f + ' -> ' + outfile
        Image.open(f).save(outfile)
print 'Done.'
