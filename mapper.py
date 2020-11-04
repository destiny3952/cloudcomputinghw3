#!/usr/bin/env python

import sys

for line in sys.stdin:

    line = line.strip()
    

    words = line.split()

    for word in words:
        if word[0]=='[' :
            date = word[1:12].split('/')
            hr = word[12:].split(':')[1]
            if date[1] == "Mar":
                date[1] = "03"
            msg = '%s-%s-%s T %s:00:00.000' % \
            (date[2], date[1], date[0], hr)

            print '%s\t%s' % (msg, 1)