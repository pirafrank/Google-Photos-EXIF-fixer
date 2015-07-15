# Google-Photos-EXIF-fixer

### Batch fix your EXIF metadata before uploads to Google Photos.

---

## Description

Google Photos doesn't recognize photos with no EXIF metadata and messes around when there's no shooting date in metadata. Using exiftool manually to fix this is pain.

gphotofix is a simple solution. It uses the filename to set shooting date in EXIF metadata. And it does it in batch, yay!

## Requirements

- Python 2.7.x *
- exiftool (You can download it [here](http://www.sno.phy.queensu.ca/~phil/exiftool/))

It works on OS X or Linux (tested on Ubuntu 13.10 and OS X 10.10.x.). Not tested on Windows. 

*Although it may work, it hasn't been tested with Python 2.6.x. Python 3 is not supported yet.

## Installation

**For OS X and Linux only**

1. Download the latest goodies from [here](https://github.com/pirafrank/Google-Photos-EXIF-fixer/archive/master.zip)

2. Unpack

3. ``` sudo cp gphotofix.py /usr/local/bin/gphotofix ```

4. ``` sudo chmod +x /usr/local/bin/gphotofix ```. You can now delete the unzipped folder. 

Enjoy!

