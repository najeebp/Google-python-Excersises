#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
	k= filename[0]
	q=open(k,'r').read()
	year=re.search(r'(<h3 align="center">Popularity in )(\d\d\d\d)',q)	
	if year:
		birth_year=year.group(2)
		print birth_year
	print "Rank   Male Name     Female Name"    
	fwrite=open('details'+birth_year,'w')
	fwrite.write('                             '+'birth year:'+birth_year+'\n')
	fwrite.write('Rank     Male Name    Female Name'+'\n')


	rank=re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w*)</td><td>(\w*)</td>',q)

	for ran in rank:
	
		fwrite.write(ran[0]+'     '+ran[1]+'    '+ran[2]+'\n')
		print ran[0]+'     '+ran[1]+'     '+ran[2]
	fwrite.close()
"""
 Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
 


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  extract_names(args)
if __name__ == '__main__':
  main()
