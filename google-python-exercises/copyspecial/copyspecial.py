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


def get_special_paths(dir):
  result = []
  filenames = os.listdir(dir)
  for filename in filenames:
    test = re.search(r'__\w+__', filename)
    if test:
      result.append(os.path.abspath(os.path.join(dir, filename)))
  return result
# +++your code here+++
# Write functions and modify main() to call them

def copy_to(path, todir):
  filenames = os.listdir(path)
  for filename in filenames:
    test = re.search(r'__\w+__', filename)
    if test:
      patg = os.path.abspath(os.path.join(path, filename))
      os.makedirs(todir)
      shutil.copy(patg, todir)



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

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
