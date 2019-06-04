#!/usr/bin/env python3

import glob
import os
import re
import sys


# Directory from which files are to be traversed
ROOT_DIR = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")

# Only files with this extension will be changed
FILE_EXTENSION = sys.argv[2] if len(sys.argv) > 2 else ""

# Files with this extensions will never be changed to LF
EXCEPTIONS = [ "ps1", "cmd", "bat", "btm" ]
EXCEPTIONS_REGEX = re.compile(r".+\.(" + "|".join(EXCEPTIONS) + ")$")

# Line endings
DOS_LINE_ENDING = b"\r\n"
UNIX_LINE_ENDING = b"\n"


for filename in glob.iglob(ROOT_DIR + "**/**", recursive=True):
    # Check whether it's a file ending with the given extensions and isn't one of
    # the excluded extensions
    if os.path.isfile(filename) and filename.endswith(FILE_EXTENSION) and not EXCEPTIONS_REGEX.match(filename):
        # Read file in binary mode to preserve original line endings
        with open(filename, "rb+") as opened_file:
            content = opened_file.read()

            # Replace CRLF with LF
            content = content.replace(DOS_LINE_ENDING, UNIX_LINE_ENDING)

            # Seek file pointer to the beginning and truncate the file
            opened_file.seek(0)
            opened_file.truncate(0)

            # Save new content to the file
            opened_file.write(content)
