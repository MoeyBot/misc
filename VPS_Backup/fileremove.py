#!/usr/bin/env python

import os

filelist = [ f for f in os.listdir(".") if f.endswith(".zip") ]
for f in filelist:
    os.remove(f)