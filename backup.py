#!/usr/bin/python
# -*- coding: ascii -*-
''' Sorts large amounts of data (e.g. backups) and filters out important files by file type. '''

__autor__ = "Adrianus Kleemans"

import os
import sys
from shutil import copy2

def main():
    src = "data"
    dst = "backup"
    filter_file = "filter.txt"

    # initialize filter
    filter = {}
    f = open(filter_file, 'r')

    for line in f:
        line = (line.split("\r")[0]).split("\n")[0].strip()
        if line.startswith("#"): category = line[1:]
        elif len(line) > 0: filter[line] = category

    print ">", len(filter), "important file types initialized."
    print "Walking tree, please wait...."

    # get all filenames
    files = []

    for t in os.walk(src):
        for f in t[2]:
            files.append(t[0] + "/" + f)

    totalfiles = len(files)
    print ">", totalfiles, "files identified."
    print "Filtering files, please wait..."

    # filter important files
    pos = 0
    while pos < len(files):
        name = files[pos]
        if name.split(".")[len(name.split("."))-1].lower() not in filter.keys():
            files.pop(pos)
        else:
            pos += 1

    impfiles = len(files)
    print "> Files succesfully filtered,", impfiles, "important files identified."
    print "Renaming files, please wait..."

    # cutting paths, leaving just the file names
    fntemp = list(files)
    i = 0
    for f in fntemp:
        fntemp[i] = f.split("/")[len(f.split("/"))-1]
        i += 1

    # replace double filenames
    filenames = []
    pos = 0
    while len(fntemp) > 0:
        el = fntemp.pop(0)
        i = 0
        el_new = el[:]
        while True:
            if el_new in filenames:
                # try for files with '.'
                try:
                    el_new = el.split(".")[len(el.split("."))-2] + "_" + str(i) + "." + el.split(".")[len(el.split("."))-1]
                    i += 1
                    continue
                except:
                    break
            break
        filenames.append(el_new)
        pos += 1
        if (len(filenames)*100/impfiles > (len(filenames)-1)*100/impfiles):
            print len(filenames)*100/impfiles, "%, remaining files:", len(fntemp)

    print "> Files successfully renamed."
    print "Creating Backup directory..."

    # make backup dir
    try:
        os.makedirs(dst)
        print "> Directory successfully created."
    except:
        print "> Directory '" + dst + "' exists already."

    print "Copying files, please wait..."

    # prepare for copying
    c = 0
    notcopied = 0
    for f in files:
        t = ""
        try:
            t = filter[filenames[c].split(".")[len(filenames[c].split(".")) - 1].lower()]
            t = dst + "/" + t
            os.mkdir(t)
        except:
            pass

        # copy files
        try:
            copy2(f, t + "/" + filenames[c])
        except:
            notcopied += 1
        c += 1

        if (c*100)/len(files) > ((c-1)*100)/len(files):
            print c*100/len(files), "%"

    print "\n>", impfiles*100/totalfiles, "% of all files copied."
    print ">", notcopied, "files were not copied due to errors."
    print "> Finished succesfully."

if __name__ == "__main__":
    main()
