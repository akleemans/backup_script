Backup Script
=============

## Introduction

Ever came across a huge pile of files (e.g. a hard disk from a friend) which you had to sort out and search for user-generated files?
Especially when dealing with messy users which spread their personal files all over the hard drive, sorting this out by hand is tedious work.

This script walks through a folder and sorts out all files with extensions mentioned in "filter.txt" and saves them back into a new folder, structured by content type.

## Purpose

The script sorts out large amount of data (e.g. backups) and filters out important files by file type.
The files are then saved into user-defined folders (one for each category), which are also in the "filter.txt"-file.
Tested for < 200k files. Not quite optimized yet.

## How to use

  1. Check and modify filter.txt for important file types to be saved (empty and lines starting with # are ignored)
  2. Place script on same file hierarchy level as your backed up files. Put them in a folder named "data".
  3. Run the script using the shell like "python backup.py".
  4. When finished, your important files are sorted by file type in a folder "backup".

## Known Bugs

* Files with multiple dots (".") get copied, but their name gets scrambled.

## License

The MIT License (MIT)

Copyright (c) 2015 Adrianus Kleemans

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
