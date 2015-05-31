#!/usr/bin/env python

import sys
import os
import re
import subprocess

pattern = "YYYY-MM-DD_hh-mm-ss"

def buildRegex(pattern):
  #print pattern,"(before)"
  pattern = pattern.replace("x","") # Clean unneeded characters
  pattern = pattern.replace("YYYY","(?P<year>\d{4})")
  pattern = pattern.replace("MM","(?P<month>\d{2})")
  pattern = pattern.replace("DD","(?P<day>\d{2})")
  pattern = pattern.replace("hh","(?P<hours>\d{2})")
  pattern = pattern.replace("mm","(?P<minutes>\d{2})")
  pattern = pattern.replace("ss","(?P<seconds>\d{2})")
  pattern = pattern.replace(".","\W+")
  pattern = pattern.replace("_","\W+")
  pattern = pattern.replace("-","\W+")
  pattern = pattern.replace(" ","\W+")
  pattern = pattern.replace("/","\W+")
  #print pattern,"(after)"
  return pattern

folder = sys.argv[1]

for filename in os.listdir(folder):
  filename = filename.replace(".jpg","")
  #print filename,"(voi siete qui)"
  pattern = buildRegex(pattern)
  prog = re.compile(pattern)
  m = prog.search(filename)
  print m
  if m:
    print(m.group("year"))