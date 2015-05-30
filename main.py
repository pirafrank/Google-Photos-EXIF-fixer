#!/usr/bin/env python

import sys
import os
import re
import subprocess

# Functions ############################################################

def core(folder,pattern):  
  #folder = sys.argv[1]
  print "Working in dir:",folder
  print "listing dir content"

  try:
    #pattern = sys.argv[2]
    file_list = os.listdir(folder)
    #print file_list
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

#if sys.argv[1] == "" or sys.argv[2] == "":
def main():
  try:
    folder=sys.argv[1]
    pattern=sys.argv[2]
    core(folder,pattern)
  except:
    print "Error: Not enough arguments!"
    print "Usage: gphotofix \"<folder path>\" <pattern>"
    print "Example: gphotofix \"/Users/francesco/Downloads/some pictures\" YYYY_MM_DD HH-MM-SS,aa"

# Program ############################################################

main()

#print datetime,"(after)"

# exiftool command:
# ExifTool.pl -overwrite_original "-DateTimeOriginal=1981:07:01 00:00:00" .\1981-07-01

