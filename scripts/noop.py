#!/usr/bin/env python

from __future__ import print_function
from pexif import JpegFile
import sys

usage = """Usage: dump_exif.py filename.jpg out.jpg"""

if len(sys.argv) != 3:
    print(usage, file=sys.stderr)
    sys.exit(1)

try:
    ef = JpegFile.fromFile(sys.argv[1])
except IOError:
    type, value, traceback = sys.exc_info()
    print("Error opening file: {0}".format(value), file=sys.stderr)
    sys.exit(1)
except JpegFile.InvalidFile:
    type, value, traceback = sys.exc_info()
    print("Error opening file: {0}".format(value), file=sys.stderr)
    sys.exit(1)

try:
    ef.writeFile(sys.argv[2])
except IOError:
    type, value, traceback = sys.exc_info()
    print("Error saving file: {0}".format(value), file=sys.stderr)
    sys.exit(1)
