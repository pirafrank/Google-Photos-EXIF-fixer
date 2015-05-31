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

def buildRegex(pattern):
  #print pattern,"(before)"
  pattern = pattern.replace("YYYY","(?P<year>\d{4})")
  pattern = pattern.replace("MM","(?P<month>\d{2})")
  pattern = pattern.replace("DD","(?P<day>\d{2})")
  pattern = pattern.replace("hh","(?P<hour>\d{2})")
  pattern = pattern.replace("mm","(?P<minute>\d{2})")
  pattern = pattern.replace("ss","(?P<second>\d{2})")
  pattern = pattern.replace(".","\D?")
  pattern = pattern.replace("_","\D?")
  pattern = pattern.replace("-","\D?")
  pattern = pattern.replace(" ","\D?")
  pattern = pattern.replace("/","\D?")
  #print pattern,"(after)"
  return pattern

def isPathExistent(folder):
  if not os.path.isdir(folder):
    return False
  else:
    return True

def pathChecker(path):
  # Check for '\' character in folder path 
  path = path.replace("\\","")
  if path[len(path)-1]==' ':
      path = path[:-1]
  return path

def fixMetadata(folder,pattern):  
  folder = pathChecker(folder)
  # pattern = patternChecker(pattern) # to implement, for people not to use to times same group (e.g HH)

  print "Working in dir:",folder
  print "Pattern is:",pattern

  try:
    for filename in os.listdir(folder):
      filename = filename.replace(".jpg","")
      pattern = buildRegex(pattern)
      prog = re.compile(pattern)
      m = prog.search(filename)
      if m:
        '''
        print(m.group("year"))
        print(m.group("month"))
        print(m.group("day"))
        print(m.group("hour"))
        print(m.group("minute"))
        print(m.group("second"))
        '''

        year=(m.group("year"))
        month=(m.group("month"))
        day=(m.group("day"))
        hour=(m.group("hour"))
        minute=(m.group("minute"))
        second=(m.group("second"))

        # Editing EXIF metadata using exiftool
        datetime = "\"-DateTimeOriginal="
        datetime=datetime+year+":"+month+":"+day+" "+hour+":"+minute+":"+second+"\""
        print datetime
        #subprocess.call(["./exiftool","-overwrite_original",datetime,filename])

  except:
    print "Error: Cannot edit EXIF metadata!"


def main():
  if len(sys.argv) < 3:
    print "Error: Not enough arguments!"
    print "Usage: gphotofix <folder path> <pattern>"
    print "Example: gphotofix /Users/francesco/Downloads/some\ pictures YYYY_MM_DD hh-mm-ss,xx"
  else:
    folder=sys.argv[1]
    if not isPathExistent(folder):
      print "Error: Path doesn't exist!"
      sys.exit()
    else:
      try:
        pattern=sys.argv[2]
        fixMetadata(folder,pattern)
      except:
        print "Error! Something wrong happened, sorry."


if __name__ == "__main__":
  main()
  #pattern = "YYYY_MM_DD"
  #buildRegex(pattern)


#print datetime,"(after)"

# exiftool command:
# ExifTool.pl -overwrite_original "-DateTimeOriginal=1981:07:01 00:00:00" .\1981-07-01

