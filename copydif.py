#!/usr/bin/env python

#----------------------------------------------------------------------
# copydif.py
#
# Copy only files that have different sizes or modification times or 
# are not present in the target directory. This will overwrite a newer 
# file in the target directory with an older file from the source 
# directory (rollback).
#
# 2011-01-14  bill@melvin.org
#----------------------------------------------------------------------

import sys
import os
import glob
import shutil
import time


def file_time_str(secs):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(secs))


def same_time_and_size(filename1, filename2):
    info1 = os.stat(filename1)
    print "  %s (%d) %s" % (file_time_str(info1.st_mtime), info1.st_size, filename1)
    if not os.path.exists(filename2):
        return False
    info2 = os.stat(filename2)
    print "  %s (%d) %s" % (file_time_str(info2.st_mtime), info2.st_size, filename2)
    if info1.st_size != info2.st_size:
        return False
    # I want this to work with shared directories on Windows and Linux 
    # (Samba). Since the file modification times may have different 
    # numeric precisions on different operating systems, compare 
    # strings representing the times instead of the actual floating 
    # point values.
    if file_time_str(info1.st_mtime) != file_time_str(info2.st_mtime):
        return False
    return True

    
def copy_differing_files(source_spec, target_dir):
    print "\nCopy files matching '%s' to '%s'\n" % (source_spec, target_dir)
    for source_filename in glob.glob(source_spec):
        target_filename = os.path.join(target_dir, os.path.split(source_filename)[1])
        if same_time_and_size(source_filename, target_filename):
            print "  Same\n"
        else:
            print "  COPY\n"
            # shutil.copy2 preserves the file modification time.
            shutil.copy2(source_filename, target_filename)      

            
if len(sys.argv) == 3:
    copy_differing_files(sys.argv[1], sys.argv[2])
else:
    print "\nUSAGE: copydif.py  Source_File_Spec  Target_Directory"
  