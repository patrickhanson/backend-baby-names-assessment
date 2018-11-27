#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse

def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    with open(filename, 'r') as file:
        baby_names = []
        read_file = file.read()
        match_object = re.search(r'Popularity in (\d{4})', read_file)
        match_baby_object = re.findall(r'<td>(\d*)</td><td>(\w+)</td><td>(\w+)</td>', read_file)
        if match_object:
            baby_year = match_object.group(1)
            baby_names.append(baby_year)
        if match_baby_object:
            for tup in match_baby_object:
                baby_names.append(tup[1] + ' ' + tup[0])
                baby_names.append(tup[2] + ' ' + tup[0])
        baby_names.sort()
        return baby_names


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    file_list = args.files

    create_summary = args.summaryfile

    for file in file_list:
        baby_list = extract_names(file)
        if create_summary:
            print 'Creating summary file for {file}'.format(file=file)
            with open(file+'.summary', 'w') as of:
                of.write('\n'.join(baby_list))
        else:
            print baby_list

if __name__ == '__main__':
    main()
