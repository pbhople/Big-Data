#!/usr/bin/env python
 
import sys

(last_key, max_val) = (None, -sys.maxint)
for line in sys.stdin:
    (key, val) = line.strip().split("\t")
    print "%s\t%s" % (key, int(val))