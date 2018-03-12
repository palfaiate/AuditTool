#!/usr/bin/env python
# # -*- coding: utf-8 -*-

import json
import sys
import os.path

if len(sys.argv) == 1:
    print "Settings File not Provided"
    sys, exit()
else:
    x = sys.argv[1]
    sFile = "settings/" + x + ".json"
    if os.path.isfile(sFile):
        with open(sFile, 'r') as j:
            files = json.load(j)
            for a in files:
                f1 = files[a]['location']
                print f1
                f = open(f1, 'r')
                for line in f:
                    c = line.find('#')
                    if c != -1:
                        c = -1
                    else:
                        for l in files[a]['settings']:
                            i = line.find(l)
                            if i != -1:
                                # this section executes if the substring is found
                                v = line.find(str(files[a]['settings'][l]))
                                print l
                                if v != -1:
                                    print 'Compliant'
                                    print line
                                else:
                                    print 'Not Compliant'
                                    print line
                                    print l, 'Correct Value should be:', files[a]['settings'][l]
                                    print ''
    else:
        print "Unable to find the Compliance file!"
