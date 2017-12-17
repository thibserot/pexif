#!/usr/bin/env python

from __future__ import print_function
from pexif import JpegFile
import sys

usage = """Usage: getgps.py filename.jpg"""

if len(sys.argv) != 2:
    print(usage, file=sys.stderr)
    sys.exit(1)

try:
    ef = JpegFile.fromFile(sys.argv[1])
    print(ef.get_geo())
except IOError:
    type, value, traceback = sys.exc_info()
    print("Error opening file: {0}".format(value), file=sys.stderr)
except JpegFile.NoSection:
    type, value, traceback = sys.exc_info()
    print("Error get GPS info: {0}".format(value), file=sys.stderr)
except JpegFile.InvalidFile:
    type, value, traceback = sys.exc_info()
    print("Error opening file: {0}".format(value), file=sys.stderr)

