#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_path(dir_name):
	paths=[]
	files=os.listdir(dir_name)
	for filee in files:
		special=re.search(r'__(\w+\w+)__',filee)
		if special:
			paths.append( os.path.abspath(filee))
	print paths
	return paths




def copy_to(path,dirr):
	print dirr
	efile=get_special_path(path)
	if not os.path.exists(dirr):
		os.mkdir(dirr)
	for each_file in efile:
		shutil.copy(each_file,os.path.abspath(dirr)) 


def zip_to(path,zippath):
	efile=get_special_path(path)
	for each_file in efile:
		cmd='zip -j'+' '+ zippath+' '+ each_file
		
		asd=commands.getstatusoutput(cmd)








def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)
  print args
  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
#    del args[0:2]
    path=args[2]
    copy_to(path,todir)
    del args[0:2]
  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    path=args[2]
    zip_to(path,tozip)
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
