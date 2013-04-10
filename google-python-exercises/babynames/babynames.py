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
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  dict = {}
  list = []
  f = open(filename, 'r')
  # Feed the file text into findall(); it returns a list of all the found strings
  year = re.search(r'(Popularity in )(\d\d\d\d)', f.read())
  print year.group(2)
  f.close
  f = open(filename, 'r')
  #names = re.findall(r'</td><td>(\w+)</td><td>(\w+)</td>', f.read())
  names = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)', f.read())
  for rank, boyname, girlname in names:
    if boyname not in names:
      dict[boyname] = rank
    if girlname not in names:
      dict[girlname] = rank
      f.close
  for k, v in sorted(dict.items()):
    print str(k) + " " + str(v)
  
  
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  # LAB(begin solution)

  # Gather all the special files
  paths = []
  for dirname in args:
    paths.extend(get_special_paths(dirname))

  if todir:
    copy_to(paths, todir)
  elif tozip:
    zip_to(paths, tozip)
  else:
    print '\n'.join(paths)
  # LAB(end solution)

if __name__ == "__main__":
  main()

