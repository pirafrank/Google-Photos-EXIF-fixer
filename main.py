#!/usr/bin/env python

import sys
import os
import re
import subprocess

try:
  import docopt
except:
  print "Error: docopt needed!"
  sys.exit()

# Regular expression that matches timestamps encoded in filenames.
timestamp_pattern = re.compile(r'''
    # Required components.
    (?P<year>\d{4} ) \D?
    (?P<month>\d{2}) \D?
    (?P<day>\d{2}  ) \D?
    (?P<hour>\d{2}  ) \D?
    (?P<minute>\d{2}) \D?
    (?P<second>\d{2})?
''', re.VERBOSE)

# Functions ############################################################

def fixMetadata(folder,pattern):  
  #folder = sys.argv[1]
  print "Working in dir:",folder
  print "listing dir content"

  try:
    # add \ removal for unix systems
    file_list = os.listdir(folder)
    for filename in file_list:
      print filename
    # test stuff
    year="2015"
    month="05"
    day="10"
    hours="11"
    minutes="00"
    seconds="00"

    # Editing EXIF metadata using exiftool
    datetime = "\"-DateTimeOriginal="
    datetime=datetime+year+":"+month+":"+day+" "+hours+":"+minutes+":"+seconds+"\""
    #subprocess.call(["./exiftool","-overwrite_original",datetime,filename])

  except:
    print "Error: Cannot edit EXIF metadata!"


def main():
  try:
    folder=sys.argv[1]
    pattern=sys.argv[2]
    fixMetadata(folder,pattern)
  except:
    print "Error: Not enough arguments!"
    print "Usage: gphotofix \"<folder path>\" <pattern>"
    print "Example: gphotofix \"/Users/francesco/Downloads/some pictures\" YYYY_MM_DD HH-MM-SS,aa"


if __name__ == "__main__":
  main()


#print datetime,"(after)"

# exiftool command:
# ExifTool.pl -overwrite_original "-DateTimeOriginal=1981:07:01 00:00:00" .\1981-07-01

